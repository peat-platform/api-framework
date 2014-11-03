__author__ = 'mpetyx'

from tastypie.api import Api

api = Api(api_name='v.04')


# Activity
from .Activity.Badge.Resources import BadgeResource
from .Activity.Checkin.Resources import CheckinResource
from .Activity.Event.Resources import EventResource
from .Activity.Measurement.Resources import MeasurementResource
from .Activity.Note.Resources import NoteResource
from .Activity.Game.Resources import GameResource
from .Activity.Nutrition.Resources import NutritionResource
from .Activity.Question.Resources import QuestionResource
from .Activity.Sleep.Resources import SleepResource
from .Activity.Status.Resources import StatusResource
from .Activity.Workout.Resources import WorkoutResource
from .Activity.Notebook.Resources import NotebookResource

api.register(BadgeResource())
api.register(CheckinResource())
api.register(EventResource())
api.register(MeasurementResource())
api.register(NoteResource())
api.register(NutritionResource())
api.register(QuestionResource())
api.register(SleepResource())
api.register(StatusResource())
api.register(WorkoutResource())
api.register(NotebookResource())
api.register(GameResource())


# Context
from .Context.Resources import ContextResource
api.register(ContextResource())


# Location
from .Location.Place.Resources import PlaceResource
from .Location.Route.Resources import RouteResource
from .Location.Travel.Resources import TravelResource

api.register(PlaceResource())
api.register(RouteResource())
api.register(TravelResource())


# Media
from .Media.Article.Resources import ArticleResource
from .Media.Audio.Resources import AudioResource
from .Media.Photo.Resources import PhotoResource
from .Media.Video.Resources import VideoResource
from .Media.File.Resources import FileResource
from .Media.Folder.Resources import FolderResource
from .Media.Page.Resources import PageResource
from .Media.Playlist.Resources import PlaylistResource

api.register(ArticleResource())
api.register(AudioResource())
api.register(PhotoResource())
api.register(VideoResource())
api.register(FileResource())
api.register(FolderResource())
api.register(PageResource())
api.register(PlaylistResource())


# Product and Services
from .Products_and_Services.Card.Resources import CardResource
from .Products_and_Services.Product.Resources import ProductResource
from .Products_and_Services.Service.Resources import ServiceResource
from .Products_and_Services.Shop.Resources import ShopResource
from .Products_and_Services.Cart.Resources import CartResource
from .Products_and_Services.Order.Resources import OrderResource
from .Products_and_Services.Wallet.Resources import WalletResource

api.register(CardResource())
api.register(ProductResource())
api.register(ServiceResource())
api.register(ShopResource())
api.register(CartResource())
api.register(OrderResource())
api.register(WalletResource())


# Profile
from .Profile.Account.Resources import AccountResource
from .Profile.Application.Resources import ApplicationResource
from .Profile.User.Resources import UserResource
from .Profile.Group.Resources import GroupResource

api.register(AccountResource())
api.register(ApplicationResource())
api.register(UserResource())
api.register(GroupResource())


# Secondary
from .Secondary.Comment.Resources import CommentResource
from .Secondary.Delivery.Resources import DeliveryResource
from .Secondary.Dislike.Resources import DislikeResource
from .Secondary.Favorite.Resources import FavoriteResource
from .Secondary.Friendship.Resources import FriendshipResource
from .Secondary.Invoice.Resources import InvoiceResource
from .Secondary.Like.Resources import LikeResource
from .Secondary.Offer.Resources import OfferResource
from .Secondary.Payment.Resources import PaymentResource
from .Secondary.QuestionOption.Resources import QuestionOptionResource
from .Secondary.Refund.Resources import RefundResource
from .Secondary.Review.Resources import ReviewResource
from .Secondary.RSVP.Resources import RSVPResource
from .Secondary.Score.Resources import ScoreResource
from .Secondary.Shipping.Resources import ShippingResource
from .Secondary.Tag.Resources import TagResource

api.register(CommentResource())
api.register(DeliveryResource())
api.register(DislikeResource())
api.register(FavoriteResource())
api.register(FriendshipResource())
api.register(InvoiceResource())
api.register(LikeResource())
api.register(OfferResource())
api.register(PaymentResource())
api.register(QuestionOptionResource())
api.register(RefundResource())
api.register(ReviewResource())
api.register(RSVPResource())
api.register(ScoreResource())
api.register(ShippingResource())
api.register(TagResource())


# Builder
from .Builder.Application.Resources import CBSResource, SocialAccountResource, SocialTokenResource
from .Builder.RegisteredDeveloperApplication.Resources import RegisteredApplicationResource


api.register(RegisteredApplicationResource())
api.register(SocialTokenResource())
api.register(SocialAccountResource())
api.register(CBSResource())


from .resources import DurationResource, PersonModelResource, FromResource, TimeResource, LocationResource
api.register(DurationResource())
api.register(PersonModelResource())
api.register(FromResource())
api.register(TimeResource())
api.register(LocationResource())



urlpatterns = api.urls
