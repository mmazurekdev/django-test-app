from django.shortcuts import render, redirect

from .models import Thing


def index(request):
    things_to_do = Thing.objects.all()
    if request.method == "POST":
        things_id = request.POST.get("id")
        if things_id:
            thing = Thing.objects.get(id=int(things_id))
            thing.make_as_done()
        else:
            description = request.POST["description"]
            thing = Thing(description=description)

        thing.save()
        return redirect("/")
    return render(request, "index.html", {"todos": things_to_do})
