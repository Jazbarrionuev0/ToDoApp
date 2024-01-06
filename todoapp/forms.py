from django import forms


class CreateNewTask(forms.Form):
    titulo = forms.CharField(label='Titulo de tarea', max_length=200)
    descripcion = forms.CharField(widget=forms.Textarea)

class EscribeTuPensamiento(forms.Form):
    title = forms.CharField(label='Titulo del pensamiento', max_length=200)
    description = forms.CharField(label='Descripcion del pensamiento', widget=forms.Textarea)
