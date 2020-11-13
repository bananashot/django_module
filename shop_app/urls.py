from django.urls import path

from shop_app.views import Registration, Login, Logout, ProductList

urlpatterns = [
    path('/', ProductList.as_view(), name='products'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('registration/', Registration.as_view(), name='registration'),
    path('create_note/', NotesCreateView.as_view(), name='create_note'),
    path('delete_note/<int:pk>/', NoteDeleteView.as_view(), name='delete_note'),
    path('share_note/<int:pk>/', NoteShareView.as_view(), name='share_note'),
    path('shared/', NotesSharedListView.as_view(), name='shared')
]