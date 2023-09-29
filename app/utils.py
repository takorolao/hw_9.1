from app.models import MyModel

def update_model_titles():
    # Цикл для изменения заголовков
    for model in MyModel.objects.all():
        model.title = f"{model.title} ({model.id})"
        model.save()

def delete_odd_titles():
    # Цикл для удаления записей с нечетными заголовками
    for model in MyModel.objects.all():
        if model.title.isdigit() and int(model.title) % 2 != 0:
            model.delete()
