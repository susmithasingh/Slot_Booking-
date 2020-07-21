# import factory, factory.fuzzy
#
# from .models import User, WashingMechine
# class UserFactory(factory.django.DjangoModelFactory):
#     class Meta:
#         model = User
#     username = factory.Sequence(lambda n: 'User%d' % n)
#     name = factory.Sequence(lambda n: 'User%d' % n)
#     profile_pic = factory.LazyAttribute(lambda obj: '%s.url' % obj.name)
#
# class WashingMechineFactory(factory.django.DjangoModelFactory)
#     class Meta:
#         model = WashingMechine
#
#      washing_mechine_id = factory.sequence(lambda n: "%d" % n)