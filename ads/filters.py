from django.db.models import Q

from .models import AdCategory

SERVICE_CATEGORIES = (
    AdCategory.SERVICES,
    AdCategory.EDUCATION,
    AdCategory.JOBS,
)

GOODS_CATEGORIES = (
    AdCategory.AUTO,
    AdCategory.FOOD,
    AdCategory.ELECTRONICS,
    AdCategory.REAL_ESTATE,
)

ALLOWED_ORDERING = {
    '-created_at',
    'price',
    '-price',
}


def apply_ad_filters(queryset, params):
    search = (params.get('search') or '').strip()
    if search:
        queryset = queryset.filter(
            Q(title__icontains=search)
            | Q(description__icontains=search)
            | Q(city__icontains=search)
            | Q(author__first_name__icontains=search)
            | Q(author__last_name__icontains=search)
        )

    city = (params.get('city') or '').strip()
    if city and city.lower() != 'all':
        queryset = queryset.filter(city__icontains=city)

    category = (params.get('category') or '').strip()
    if category and category != 'all' and category in AdCategory.values:
        queryset = queryset.filter(category=category)

    listing_type = (params.get('type') or '').strip()
    if listing_type == 'service':
        queryset = queryset.filter(category__in=SERVICE_CATEGORIES)
    elif listing_type == 'goods':
        queryset = queryset.filter(category__in=GOODS_CATEGORIES)
    elif listing_type == 'urgent':
        queryset = queryset.filter(is_urgent=True)

    ordering = (params.get('ordering') or '-created_at').strip()
    if ordering not in ALLOWED_ORDERING:
        ordering = '-created_at'

    return queryset.order_by(ordering)
