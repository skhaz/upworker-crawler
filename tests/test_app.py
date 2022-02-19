from app.main import create_app

app = create_app()


def test_should_return_not_found_on_index():
    with app.test_client() as client:
        response = client.get("/")

        assert response.status_code == 404
