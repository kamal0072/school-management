from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout,Fieldset,ButtonHolder
from crispy_forms.bootstrap import InlineField


class Studentform(forms.Form):
    name=forms.CharField(label="Your Name:",help_text="Write Your name here")
    address=forms.CharField(max_length=15,help_text="Write Your Address here")
    email=forms.EmailField(label="Email Address", help_text='write your email here')
    message=forms.CharField(
        max_length=2000,
        widget=forms.Textarea(),
        help_text='Write Your message here'
    )
    source=forms.CharField(
        max_length=50,
        widget=forms.HiddenInput()
    )
    def clean(self):
        cleaned_data=super(Studentform,self.clean)
        name=cleaned_data.get['name']
        address=cleaned_data.get['address']
        email=cleaned_data.get['email']
        message=cleaned_data.get['message']
        if not name and not address and not email and not message:
            raise forms.ValidationError("Please write something the form")

class ExampleForm(forms.Form):
    like_website = forms.TypedChoiceField(
        label = "Do you like this website?",
        choices = ((1, "Yes"), (0, "No")),
        coerce = lambda x: bool(int(x)),
        widget = forms.RadioSelect,
        initial = '1',
        required = True,
    )

    favorite_food = forms.CharField(
        label = "What is your favorite food?",
        max_length = 80,
        required = True,
        help_text='Give your fav food',
    )

    favorite_color = forms.CharField(
        label = "What is your favorite color?",
        max_length = 80,
        required = True,
        help_text='Choose Your fav color',
    )

    favorite_number = forms.IntegerField(
        label = "Favorite number",
        required = False,
        help_text='Choose your fav number',

    )

    notes = forms.CharField(
        label = "Additional notes or feedback",
        required = False,
    )
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = "id-exampleform"
        self.helper.form_class = "blueForms"
        self.helper.form_method = "post"
        self.helper.form_action = "submit_survey"
        self.helper.add_input(Submit('submit','Submit'))
        self.helper.layout=Layout(
            Fieldset(
                'first arg is the legend of the fieldset',
                'like_website',
                'favorite_number',
                'favorite_color',
                'favorite_food',
                'notes'
            ),
            ButtonHolder(
                Submit('submit','Submit',css_class='button white')
            )
        )
