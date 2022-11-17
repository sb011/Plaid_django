import plaid
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .serializers import AccessToken
from .models import Item
from .tasks import fetch_transactions
from rest_framework.response import Response
from rest_framework import status
from .keys import PLAID_CLIENT_ID, PLAID_SECRET, PLAID_PUBLIC_KEY, PLAID_ENV

client = plaid.Client(client_id=PLAID_CLIENT_ID, secret=PLAID_SECRET,
                      public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV, api_version='2022-11-17')


class get_access_token(APIView):
    """
    Exchanges Public token for access token
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        request_data = request.POST
        public_token = request_data.get('public_token')
        try:
            exchange_response = client.Item.public_token.exchange(public_token)
            serializer = AccessToken(data=exchange_response)
            if serializer.is_valid():
                access_token = serializer.validated_data['access_token']
                item = Item.objects.create(access_token=access_token,
                                           item_id=serializer.validated_data['item_id'],
                                           user=self.request.user
                                           )
                item.save()

                # Async Task
                fetch_transactions.delay(access_token)

        except plaid.errors.PlaidError as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return Response(data=exchange_response, status=status.HTTP_200_OK)
