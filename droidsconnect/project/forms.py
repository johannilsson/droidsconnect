from django import newforms as forms

class ProjectForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea, help_text="Markdown syntax")
    type = forms.ChoiceField(choices=[["App", "App"], ["Game", "Game"]])
    needs_developer = forms.BooleanField(required=False)
    needs_artist = forms.BooleanField(required=False)
    needs_copywriter = forms.BooleanField(required=False)
    vcs_url = forms.URLField(required=False, help_text="Eg: GitHub, bitbucket, Google Code etc")
    project_url = forms.URLField(required=False)
    package_name = forms.CharField(required=False, help_text="The package name if the application is available on Android Market")

