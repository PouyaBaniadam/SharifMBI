from Us.models import SocialMedia


def social_media(request):
    social_media = SocialMedia.objects.last()

    context = {
        "social_media": social_media
    }

    return context
