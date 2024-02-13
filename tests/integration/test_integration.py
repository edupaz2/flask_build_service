from project import create_app

def test_home_page():
    flask_app = create_app(testing=True)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/')
        assert response.status_code == 200

def test_cmake_example_project():
    flask_app = create_app(testing=True)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/build_repo/https://github.com/edupaz2/cmake_example_project.git')
        assert response.status_code == 200

def test_wrong_cmake_example_project():
    flask_app = create_app(testing=True)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/build_repo/https://this_is_not_a_repo.git')
        assert response.status_code == 400

def test_empty_cmake_example_project():
    flask_app = create_app(testing=True)

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        response = test_client.get('/build_repo/github.com/edupaz2/edupaz2.git')
        assert response.status_code == 400
