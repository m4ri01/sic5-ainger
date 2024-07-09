from . import create_app, db
from .models import Student, Book, Loan
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect

main = Blueprint('main', __name__)
csrf = CSRFProtect()

@main.route('/')
def index():
    return render_template('home.html')


@main.route('/rekomendasi')
def rekomendasi_buku():
    return render_template('rekomendasi_buku.html')

@main.route('/peminjaman')
def menu_peminjaman():
    return render_template('menu_peminjaman.html')

@main.route('/pengembalian')
def menu_pengembalian():
    return render_template('menu_pengembalian.html')

@main.route('/registrasi', methods=['GET', 'POST'])
def registrasi():
    if request.method == 'POST':
        name = request.form.get('name')
        class_name = request.form.get('class_name')
        address = request.form.get('address')
        fingerprint = request.form.get('fingerprint')

        if not (name and class_name and address and fingerprint):
            flash('Please fill out all fields', 'error')
        else:
            new_student = Student(name=name, class_name=class_name, address=address, fingerprint=fingerprint)
            db.session.add(new_student)
            db.session.commit()
            flash('Registrasi berhasil!', 'success')
            return redirect(url_for('main.index'))

    return render_template('registrasi.html')


@main.route('/get_students/<string:fingerprint>', methods=['GET'])
def get_students(fingerprint):
    student = Student.query.filter_by(fingerprint=fingerprint).first()
    if student:
        return {
            'message': 'success',
            'id': student.id,
            'name': student.name,
            'class_name': student.class_name,
            'address': student.address,
            'fingerprint': student.fingerprint
        }
    else:
        return {
            'message': 'failed'
        }
