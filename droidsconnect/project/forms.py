from django import newforms as forms

class ProjectForm(forms.Form):
    title = forms.CharField(label="Project Title")
    description = forms.CharField(widget=forms.Textarea, help_text="Markdown syntax")
    type = forms.ChoiceField(choices=[["App", "an app"], ["Game", "a game"]])
    
    needs_developer = forms.BooleanField(required=False, label="Looking for a developer to:")
    needs_developer_list = forms.CharField(widget=forms.Textarea, required=False, label="List of things you'd like the programmer to do.")
    
    needs_artist = forms.BooleanField(required=False, label="Looking for a graphics artist to:")
    needs_artist_list = forms.CharField(widget=forms.Textarea, required=False, label="List of things you'd like the artist to do.")
    
    needs_copywriter = forms.BooleanField(required=False, label="Looking for a copywriter to:")
    needs_copywriter_list = forms.CharField(widget=forms.Textarea, required=False, label="List of things you'd like the copywriter to do.")
    
    vcs_url = forms.URLField(required=False, label="VCS Link (Eg: GitHub, Google Code etc.)")
    project_url = forms.URLField(required=False, label="Official website")
    package_name = forms.CharField(required=False, label="Package name (Market QR code)")

