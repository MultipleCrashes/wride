In [1]: from django.db.models import *

In [2]: from rideapp.models import *

In [3]: User.objects.all()
Out[3]: [<User: User object>, <User: User object>, <User: User object>]

In [4]: u = User.objects.all()
