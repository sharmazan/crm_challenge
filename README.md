# crm_challenge
Django backend to list and search AppUser, Address and CustomerRelationship records.

## Models
### AppUser
- id
- first_name
- last_name
- gender
- customer_id
- phone_number
- created
- address_id (FK)
- birthday
- last_updated

### Address
- id
- street
- street_number
- city_code
- city
- country

### CustomerRelationship
- id
- appuser_id (FK)
- points
- created
- last_activity

# TODO
- ___Set up a Django project - done___
- ___Add models - done___
- Write a management command to insert random values. Add 100 records for testing
- Add a View for the data structure that join all 3 tables and return JsonResponse with attributes from all 3 tables
- Add sort, filter and list by any field
- Add pagination
- Add 3 million of data entries (AppUser, Address and a CustomerRelationship) with random values
- Measure how long it takes to return results: 
    - Load the first page without filters
    - Filter by a name
    - Sort by points and filter by city
    - Sort by points, filter by city, page=5 with 50 records in each
- Add performance optimisations
- Compare results with initial benchmarks

# Notes
1. This task implemented using pure Django. For the production purposes it's better use [Django Cookiecutter template](https://cookiecutter-django.readthedocs.io/en/latest/) with Django Rest Framework. 
