from django import forms

from .models import Reviews, Rating, RatingStar


class ReviewForms(forms.ModelForm):
    """Review Form"""
    class Meta():
        model = Reviews
        fields = ("name", "email", "text")


class RatingForm(forms.ModelForm):
    """Adding Rating Frms"""
    star = forms.ModelChoiceField(
        queryset=RatingStar.objects.all(), widget=forms.RadioSelect(), empty_label=None
    )

    class Meta:
        model = Rating
        fields = ("star",)