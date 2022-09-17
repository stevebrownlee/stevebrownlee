import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from libraryapp.models import Librarian
from libraryapp.models import model_factory
from ..connection import Connection


@login_required
def list_librarians(request):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = model_factory(Librarian)
        db_cursor = conn.cursor()

        db_cursor.execute("""
        select
            l.id,
            l.location_id,
            l.user_id,
            u.first_name,
            u.last_name,
            u.email
        from libraryapp_librarian l
        join auth_user u on l.user_id = u.id
        """)

        all_librarians = db_cursor.fetchall()

    template_name = 'librarians/list.html'
    return render(request, template_name, {'all_librarians': all_librarians})
