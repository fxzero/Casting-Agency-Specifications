'''
Tests for jwt flask app.
'''
import os                                   
import json
import pytest

import app

SECRET = 'TestSecret'
TOKEN_EP = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJFWXpNRVJGUWpKRFFUUkdOVE0zTXpKQ1JqQXpOakpETXpVd1EwRTVNamhHTmpjNU1qUkdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcmJxdHI3aS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRkZDIzNWQ3YjNlZmIwY2QwYWYzODQ2IiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1NzkyMjYzMzksImV4cCI6MTU3OTMxMjczOSwiYXpwIjoicXBnSUJzS01sVnczRVpZcG1PYWZ2MHdZaHFmd1RCZ04iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.XQEt1QqVBuSATU9J1jkUgBaRm8o90dl2rK_MZ0o91RUA-zH7lM_Aj0FRCNtzKaewRHnItXtpGMhi7OxkO1Etqd6mZVLLYl24BdiDXAWaePORaimRvVdR1jEgWRRfVqFkrYnFLb8H8cB2Zn8daWw7PwSGNMHAeC3CqhzSSZyAb_ZlHvPMxvwE-iJvJ3UaZQWcPjghz_gTiDrR7_-eHVuV1FbXKCKQNW0aSGE0aGi4P4q_-Hjv7ejb_PIdu61KxRacifpxq8YkADR0QXQMLL7i85JvLUtXTeRqbfP6FIPZ0rSLUIIUB-kIozgpFOLiC40H6tBZH_QPbwiOCcu24nX9Gw'
TOKEN_CD = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJFWXpNRVJGUWpKRFFUUkdOVE0zTXpKQ1JqQXpOakpETXpVd1EwRTVNamhHTmpjNU1qUkdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcmJxdHI3aS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRkY2UwNjE3YjNlZmIwY2QwYWYzMzZhIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1NzkyMzcwNTYsImV4cCI6MTU3OTMyMzQ1NiwiYXpwIjoicXBnSUJzS01sVnczRVpZcG1PYWZ2MHdZaHFmd1RCZ04iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.wUqSB8SI9Kb4uM75dj4GXRyyzQd55r0ShHtKuGT6Lype3vpQD8kzOLEZTTPW3GNu9JuJnNQBJlV6cmnWb4hjL5oHNfFIQn5TiSaQ4LP_djTgp8MRjrX5lEnb2ffyGGvWpSq0jrNrM7bZzpMh_jyvkh4uelbjUSrPgRrq0nk1o5KoKCGWjvzbyDKh8Xd-sWL65fVHdlHFAa2XdU_k8IPJrzLGgukaOh_j0P2KM8bW5tPOeffS-P44O5YfHR7YFnBv-SDBGgAlSyVUnzQDBBgxf0WEZXZ3Bc0jr2rTcK_OhN4fvN3q5BQoOztcEQxZjOA5_RDHIeB45XWspykJ_a6kkQ'
TOKEN_CA = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlJFWXpNRVJGUWpKRFFUUkdOVE0zTXpKQ1JqQXpOakpETXpVd1EwRTVNamhHTmpjNU1qUkdNUSJ9.eyJpc3MiOiJodHRwczovL2Rldi1lcmJxdHI3aS5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NWRkN2UxOTAyOTkwNzcwZjJhMzI5Y2ZjIiwiYXVkIjoiY2FzdGluZ19hZ2VuY3kiLCJpYXQiOjE1NzkyMzcxNTgsImV4cCI6MTU3OTMyMzU1OCwiYXpwIjoicXBnSUJzS01sVnczRVpZcG1PYWZ2MHdZaHFmd1RCZ04iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.smGD401CNbiOrlQobTy4GMbtQ38TS5BDwDXfKPW8Hibc2MKyuIbfRoA-dA6TKz-0iVHEonRCunTUUQu6cBSq0UtUTcN_a_Eb4H8IgxdRg8ED3cOUuOfFomkiqXEeKrvwbHwX6O5RAGhuvA5ceMDA9xdCk__s5pEv2pzhM3kXt7-Fl2E1Qgrhxl4D8F1-ABlNJ3_ySC_D-ST_pnSFQy0esVVpqJbSvzNtlOgxNo3-215kZe-XenKHsPQiBQrJIQv64qtBmpee_oouIe4ThvmRTbWaLI1Axs2ZTXwdsfwD-oezvMz_n5c-Jt7kZft4ftPDAgbvTGY0dYBLdwF2Z6VZTQ'

@pytest.fixture
def client():
    os.environ['JWT_SECRET'] = SECRET
    app.APP.config['TESTING'] = True
    client = app.APP.test_client()

    yield client

# Success test

def test_get_actors_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.get('/actors', headers=headers)
    assert response.status_code in (200, 404) 

def test_post_actors_success(client):
    body = {'name':'actor1',
            'age':25,
            'gender':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.post('/actors',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 200
    assert response.json['actors']['name'] == 'actor1'

def test_update_actors_success(client):
    body = {'name':'actor3',
            'age':28,
            'gender':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.patch('/actors/1',
                            data=json.dumps(body),
                            content_type='application/json',
                            headers=headers)
    assert response.status_code == 200
    assert response.json['actors']['name'] == 'actor3'

def test_delete_actors_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.delete('/actors/1', headers=headers)
    assert response.status_code == 200
    assert response.json['actors'] == '1'

def test_get_movies_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.get('/movies', headers=headers)
    assert response.status_code in (200, 404)

def test_post_movies_success(client):
    body = {'title':'movie1',
            'release_date':'2019-12-11'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.post('/movies',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 200
    assert response.json['movies']['title'] == 'movie1'

def test_update_movies_success(client):
    body = {'title':'movie2',
            'release_date':'2019-11-11'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.patch('/movies/1',
                            data=json.dumps(body),
                            content_type='application/json',
                            headers=headers)
    assert response.status_code == 200
    assert response.json['movies']['title'] == 'movie2'

def test_delete_movies_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.delete('/movies/1', headers=headers)
    assert response.status_code == 200
    assert response.json['movies'] == '1'

# Error test
def test_get_actors_error(client):
    response = client.get('/actors')
    assert response.status_code == 401

def test_post_actors_error(client):
    body = {'a':'actor1',
            'b':25,
            'c':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.post('/actors',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 422

def test_update_actors_error(client):
    body = {'a':'actor1',
            'b':25,
            'c':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.patch('/actors/1',
                            data=json.dumps(body),
                            content_type='application/json',
                            headers=headers)
    assert response.status_code == 422

def test_delete_actors_error(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.delete('/actors/100', headers=headers)
    assert response.status_code == 404

def test_get_movies_error(client):
    response = client.get('/movies')
    assert response.status_code == 401

def test_post_movies_error(client):
    body = {'a':'movie1',
            'b':'2019-12-11'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.post('/movies',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 422

def test_update_movies_error(client):
    body = {'a':'movie2',
            'b':'2019-11-11'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.patch('/movies/1',
                            data=json.dumps(body),
                            content_type='application/json',
                            headers=headers)
    assert response.status_code == 422

def test_delete_movies_error(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.delete('/movies/100', headers=headers)
    assert response.status_code == 404

# Auth test
# Test for Casting Assistant
def test_get_actors_ca_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_CA}'}
    response = client.get('/actors', headers=headers)
    assert response.status_code in (200, 404)

def test_post_actors_ca_error(client):
    body = {'name':'actor1',
            'age':25,
            'gender':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_CA}'}
    response = client.post('/actors',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 401

# Test for Casting Director
def test_post_actors_cd_success(client):
    body = {'name':'actor1',
            'age':25,
            'gender':'M'}
    headers = {'Authorization': f'Bearer {TOKEN_CD}'}
    response = client.post('/actors',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 200
    assert response.json['actors']['name'] == 'actor1'

def test_post_movies_cd_error(client):
    body = {'title':'movie1',
            'release_date':'2019-12-11'}
    headers = {'Authorization': f'Bearer {TOKEN_CD}'}
    response = client.post('/movies',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 401

# Test for Executive Producer
def test_post_movies_ep_success(client):
    body = {'title':'movie1',
            'release_date':'2019-12-11'}
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.post('/movies',
                           data=json.dumps(body),
                           content_type='application/json',
                           headers=headers)
    assert response.status_code == 200
    assert response.json['movies']['title'] == 'movie1'

def test_delete_movies_ep_success(client):
    headers = {'Authorization': f'Bearer {TOKEN_EP}'}
    response = client.delete('/movies/1', headers=headers)
    assert response.status_code in (200, 404)