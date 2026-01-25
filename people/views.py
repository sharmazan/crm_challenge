import pprint
from django.db import connection
from django.http import JsonResponse
from .models import AppUser, CustomerRelationship, Address

# Create your views here.
def index(request):
    users_qs = AppUser.objects
    # users_qs = users_qs.select_related("address")
    # users_qs = users_qs.prefetch_related("customerrelationship_set")
    users_qs = users_qs.all()[:5]
    data = []
    for u in users_qs:
        data.append({
            "first_name": u.first_name,
            "last_name": u.last_name,
            "gender": u.gender,
            "customer_id": u.customer_id,
            "phone_number": u.phone_number,
            "created": u.created,
            "address": u.address,
            "birthday": u.birthday,
            "last_updated": u.last_updated,
            "address": {
                "country": u.address.country,
                "city_code": u.address.city_code,
                "city": u.address.city,
                "street": u.address.street,
                "street_number": u.address.street_number,
            },
            "customer_relationships": [
                {
                    "points": cr.points,
                    "created": cr.created,
                    "last_activity": cr.last_activity,
                }
                for cr in u.customerrelationship_set.all()
            ],
        })
    queries = connection.queries
    print(40*"*")
    pprint.pp(queries)
    print(40*"*")
    return JsonResponse(data, safe=False)
