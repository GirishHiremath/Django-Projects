from django.shortcuts import render

def my_fav(request):
    name="shreenath"
    player="Dhoni"
    animal="Lion"
    sub="python"
    d={'name1':name,'player1':player,'animal1':animal,'sub1':sub}
    return render(request,'staticApp/1.html',d)
    
