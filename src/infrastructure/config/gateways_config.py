from infrastructure.gateways_impl.canteens_gateway_impl import CanteensGatewayImpl
from infrastructure.gateways_impl.notification_gateway_impl import NotificationGatewayImpl
from infrastructure.gateways_impl.stadburo_gateway_impl import StadburoGatewayImpl
from infrastructure.gateways_impl.users_gateway_impl import UsersGatewayImpl

users_gateway = UsersGatewayImpl()
stadburo_gateway = StadburoGatewayImpl()
canteens_gateway = CanteensGatewayImpl()
notification_gateway = NotificationGatewayImpl()
