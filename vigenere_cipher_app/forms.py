from django import forms
class VigenereCipherForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Text to Encrypt/Decrypt')
    word = forms.CharField(max_length=100, label='word')
    action = forms.ChoiceField(choices=[('encrypt', 'Encrypt'), ('decrypt', 'Decrypt')], widget=forms.RadioSelect)
