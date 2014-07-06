from django import forms


class InfoTipForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_mail(self):
        subject = self.cleaned_data['subject']
        print "I would totally send mail now", subject
