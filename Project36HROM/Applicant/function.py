def handle_uploaded_file(f):
    with open('app36/static/resume' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
