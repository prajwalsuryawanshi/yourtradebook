from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Trade
from .forms import TradeForm
from django.contrib.auth import login
from django.contrib.auth import logout as auth_logout
from .forms import RegisterForm

@login_required
def dashboard(request):
    trades = Trade.objects.filter(user=request.user)
    lifetime_pl = Trade.calculate_lifetime_pl(request.user)
    user_details = {
        'username': request.user.username,
        'email': request.user.email
    }
    return render(request, 'trades/dashboard.html', {
        'trades': trades,
        'lifetime_pl': lifetime_pl,
        'user_details': user_details,
    })

@login_required
def logout(request):
    auth_logout(request)
    return redirect('/') 

# Other views remain the same
@login_required
def add_trade(request):
    if request.method == 'POST':
        form = TradeForm(request.POST)
        if form.is_valid():
            trade = form.save(commit=False)
            trade.user = request.user
            trade.save()
            return redirect('dashboard')
    else:
        form = TradeForm()
    return render(request, 'trades/add_trade.html', {'form': form})

@login_required
def edit_trade(request, id):
    trade = get_object_or_404(Trade, id=id, user=request.user)
    if request.method == 'POST':
        form = TradeForm(request.POST, instance=trade)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = TradeForm(instance=trade)
    return render(request, 'trades/edit_trade.html', {'form': form})

@login_required
def delete_trade(request, id):
    trade = get_object_or_404(Trade, id=id, user=request.user)
    if request.method == 'POST':
        trade.delete()
        return redirect('dashboard')
    return render(request, 'trades/delete_trade.html', {'trade': trade})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})