from django.shortcuts import render
import psycopg2
from .forms import RegForm, LogInForm
import datetime
from . import ii


conn = psycopg2.connect(database="bakerydb", user="postgres", password="Wake_Pig_2003", host="localhost", port="5432")


def index(request):
    return render(request, 'main/index.html')


def contacts(request):
    return render(request, 'main/contacts.html')


def sales(request):
    return render(request, 'main/sales.html')


def menu(request):
    recomendations = ii.give_rec()
    cur0 = conn.cursor()
    cur0.execute("SELECT * FROM items WHERE item_id IN (" + str(recomendations[0]) + ", " + str(recomendations[1]) + ")")
    s0 = cur0.fetchall()
    cur = conn.cursor()
    cur.execute("SELECT * FROM items")
    s = cur.fetchall()
    date = {
        's': s,
        's0': s0
    }
    return render(request, 'main/menu.html', date)


def enter(request):
    error = ""
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            s = ""
            cur = conn.cursor()
            cur.execute(s)
            conn.commit()
        else:
            error = "Неверные данные"
    else:
        form = LogInForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/enter.html', data)


def registration(request):
    error = ""
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            birth = form.cleaned_data['birth']
            adress = form.cleaned_data['adress']
            mail = form.cleaned_data['mail']
            phone = form.cleaned_data['phone']
            password = form.cleaned_data['password']
            s = "INSERT INTO customers (cust_name, cust_surname, cust_birth, cust_adress, cust_password," +\
                "cust_regdate, cust_score, cust_mail, cust_phone) VALUES ('" + str(name) + "', '" + str(surname) +\
                "', '" + str(birth) + "', '" + str(adress) + "', '" + str(password) + "', '" +\
                str(datetime.date.today().isoformat()) + "', '" + str(0) + "', '" + str(mail) + "', '" +\
                str(phone) + "')"
            cur = conn.cursor()
            cur.execute(s)
            conn.commit()
        else:
            error = "Неверные данные"
    else:
        form = RegForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'main/registration.html', data)
