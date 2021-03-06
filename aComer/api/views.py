#from django.shortcuts import render
from rest_framework import generics
# Create your views here.
from fonda.models import (
    Restaurant,
    Plate,
    Order,
    MenuPlate,
    Menu,
    MenuPlate,
    )
from user.models import (
    Client,
    ClientAddress,
    Rating,
)
from .serializers import (
    #restaurants
    RestaurantListSerializer,
    RestaurantSerializer,
    RestaurantAddressSerializer,
    RestaurantOrderSerializer,
    RestaurantMenuSerializer,
    RestaurantPlatesSerializer,
    RestaurantAddressListSerializer,
    RestaurantAddressListsSerializer,
    #plates
    PlateListSerializer,
    PlateSerializer,
    #orders
    OrderListSerializer,
    #restaurant addresses
    RestaurantCreateSerializer,
    RestaurantAddressesSerializer,
    #menu
    MenusListSerializer,
    MenusSerializer,
    MenusUpdateSerializer,
    #MenusplateunicSerializer,
    #client
    ClientsListSerializer,
    ClientsSerializer,
    ClientAddressListSerializer,
    ClientCreateSerializer,
    #client addresses
    ClientAddressesListSerializer,
    ClientAddressesSerializer,
    #raitings
    RaitingsListSerializer,
    #menuPlate
    MenuPlateSerializer,
    )

#RestaurantViews
class ListRestaurantsAPIView(generics.ListAPIView):
    queryset = Restaurant.objects.all()#.order_by("created_at")
    serializer_class = RestaurantSerializer 

class CreateRestaurantAPIView(generics.CreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer

class RetrieveRestaurantAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantListSerializer   

class UpdateRestaurantAPIView(generics.UpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantCreateSerializer

class DeleteRestaurantAPIView(generics.DestroyAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer 

class CreateRestaurantAddressesAPIView(generics.CreateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = RestaurantCreateSerializer

####

class RetrieveRestaurantAddressAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantAddressListSerializer

class RetrieveRestaurantOrdersAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantOrderSerializer


class RetrieveRestaurantMenusAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantMenuSerializer


class RetrieveRestaurantPlatesAPIView(generics.RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantPlatesSerializer


#PlateView

class ListPlatesAPIView(generics.ListAPIView):
    queryset = Plate.objects.all()#.order_by("created_at")
    serializer_class = PlateSerializer

class CreatePlatesAPIView(generics.CreateAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class RetrievePlatesAPIView(generics.RetrieveAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class UpdatePlatesAPIView(generics.UpdateAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateListSerializer

class DeletePlatesAPIView(generics.DestroyAPIView):
    queryset = Plate.objects.all()
    serializer_class = PlateSerializer

#Order

class ListOrdersAPIView(generics.ListAPIView):
    queryset = Order.objects.all()#.order_by("created_at")
    serializer_class = OrderListSerializer

class CreateOrdersAPIView(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class RetrieveOrdersAPIView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class UpdateOrdersAPIView(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

class DeleteOrdersAPIView(generics.DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderListSerializer

#RestaurantAddres

class ListRestaurantAddressesAPIView(generics.ListAPIView):
    queryset = MenuPlate.objects.all()#.order_by("created_at")
    serializer_class = RestaurantAddressListsSerializer



class CreateRestAddressesAPIView(generics.CreateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = RestaurantAddressSerializer

class RetrieveRestaurantAddressesAPIView(generics.RetrieveAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = RestaurantAddressesSerializer

class RetrieveUpdateRestaurantAddressesAPIView(generics.RetrieveUpdateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = RestaurantAddressesSerializer

class RetrieveDeleteRestaurantAddressesAPIView(generics.RetrieveDestroyAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = RestaurantAddressesSerializer


#Menu
class ListMenusAPIView(generics.ListAPIView):
    queryset = Menu.objects.all()#.order_by("created_at")
    serializer_class = MenusSerializer

class CreateMenusAPIView(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusListSerializer

class RetrieveMenusAPIView(generics.RetrieveAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusListSerializer

class UpdateMenusAPIView(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusUpdateSerializer

class DeleteMenusAPIView(generics.DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenusSerializer

# class CreateMenuUnicAPIView(generics.CreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenusplateunicSerializer

#client

class ListClientsAPIView(generics.ListAPIView):
    queryset = Client.objects.all()#.order_by("created_at")
    serializer_class = ClientsSerializer

class CreateClientAPIView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer

class RetrieveClientsAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer

class UpdateClientsAPIView(generics.UpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsListSerializer

class DeleteClientsAPIView(generics.DestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer

class ClientAddressAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientAddressListSerializer

class ClientOrdersAPIView(generics.RetrieveAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientAddressListSerializer

class CreateClientAddressesAPIView(generics.CreateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = ClientCreateSerializer

#client address

class ListAddressesAPIView(generics.ListAPIView):
    queryset = ClientAddress.objects.all()#.order_by("created_at")
    serializer_class = ClientAddressesSerializer

class CreateAddressesAPIView(generics.CreateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

class RetrieveAddressesAPIView(generics.RetrieveAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer


class RetrieveDeleteAddressesAPIView(generics.RetrieveDestroyAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

class RetrieveUpdateAddressesAPIView(generics.RetrieveUpdateAPIView):
    queryset = ClientAddress.objects.all()
    serializer_class = ClientAddressesListSerializer

#ratings

class ListRatingsAPIView(generics.ListAPIView):
    queryset = Rating.objects.all()#.order_by("created_at")
    serializer_class = RaitingsListSerializer

class CreateRatingsAPIView(generics.CreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class RetrieveRatingsAPIView(generics.RetrieveAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class UpdateRatingsAPIView(generics.UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

class DeleteRatingsAPIView(generics.DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RaitingsListSerializer

#menuPLate

class ListMenuPlateAPIView(generics.ListAPIView):
    queryset = MenuPlate.objects.all()#.order_by("created_at")
    serializer_class = MenuPlateSerializer

class CreateMenuPlateAPIView(generics.CreateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = MenuPlateSerializer

class RetrieveMenuPlateAPIView(generics.RetrieveAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = MenuPlateSerializer

class UpdateMenuPlateAPIView(generics.UpdateAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = MenuPlateSerializer

class DeleteMenuPlateAPIView(generics.DestroyAPIView):
    queryset = MenuPlate.objects.all()
    serializer_class = MenuPlateSerializer