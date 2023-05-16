"""Test list of ad resources"""
import pytest
from flask_sqlalchemy.pagination import Pagination

from api.models import Ad
from test.factories import AdFactory


@pytest.fixture()
def ads(size, session):
    return [AdFactory.create() for _ix in range(size)]


@pytest.mark.parametrize("size", (20,))
def test_success_ad_listing_first_page(client, ads, mocker, size):
    """Tests success ad listing when records exist"""

    return_value = Ad.query.order_by(Ad.id.desc())
    mocked_repository = mocker.patch(
        "api.repositories.ads.list", return_value=return_value
    )
    response = client.get("/ads/", headers={"Content-Type": "application/json"})
    assert response.status == "200 OK"
    mocked_repository.assert_called_once()
    data = response.get_json()
    assert data["total"] == 20
    assert not data["previous"]
    assert data["next"] == "/api/ads/?page=2&size=10"
    assert len(data["results"]) == 10


@pytest.mark.parametrize("size", (20,))
def test_success_ad_listing_last_page(client, ads, mocker, size):
    """Tests success ad listing when records exist"""

    return_value = Ad.query.order_by(Ad.id.desc())

    mocked_repository = mocker.patch(
        "api.repositories.ads.list", return_value=return_value
    )
    response = client.get(
        "/ads/?page=2&limit=1", headers={"Content-Type": "application/json"}
    )
    assert response.status == "200 OK"
    mocked_repository.assert_called_once()
    data = response.get_json()
    assert data["total"] == 20
    assert not data["next"]
    assert data["previous"] == "/api/ads/?page=1&size=10"
    assert len(data["results"]) == 10


def test_success_ad_listing_no_records(client, session, mocker):
    """When there are no records display empty results"""
    return_value = Ad.query.order_by(Ad.id.desc())

    mocked_repository = mocker.patch(
        "api.repositories.ads.list", return_value=return_value
    )
    response = client.get("/ads/", headers={"Content-Type": "application/json"})
    assert response.status == "200 OK"
    mocked_repository.assert_called_once()
    data = response.get_json()
    assert data["total"] == 0
    assert not data["previous"]
    assert not data["next"]
    assert len(data["results"]) == 0


@pytest.mark.parametrize("size", (20,))
def test_success_add_listing_page_no_records(client, session, mocker, size):
    """Specify page of records via url retrieves correct set"""
    return_value = Ad.query.order_by(Ad.id.desc())

    mocked_repository = mocker.patch(
        "api.repositories.ads.list", return_value=return_value
    )
    response = client.get("/ads/", headers={"Content-Type": "application/json"})
    assert response.status == "200 OK"
    mocked_repository.assert_called_once()
    data = response.get_json()
    assert data["total"] == 0
    assert not data["previous"]
    assert not data["next"]
    assert len(data["results"]) == 0


@pytest.mark.parametrize("page", ("one",))
def test_error_specify_bad_page_param(client, session, mocker, page):
    """When specify an invalid value for page it raises an API error"""
    response = client.get(
        "/ads/",
        query_string={"page": page},
        headers={"Content-Type": "application/json"},
    )
    assert response.status == "400 BAD REQUEST"
    assert response.get_json() == {"message": {"page": "Current page"}}


@pytest.mark.parametrize("size", (10, 20))
def test_success_add_listing_size_records(size, client, ads):
    """Specify per_page of records via url retrieves correct set"""
    response = client.get(
        "/ads/",
        query_string={"size": size},
        headers={"Content-Type": "application/json"},
    )
    assert response.status == "200 OK"
    data = response.get_json()
    assert data["total"] == size
    assert not data["previous"]
    assert not data["next"]
    assert len(data["results"]) == size


@pytest.mark.parametrize("size", ("one",))
def test_error_specify_bad_size_page(client, size):
    """When specify an invalid value for size it raises an API error"""
    response = client.get(
        "/ads/",
        query_string={"size": size},
        headers={"Content-Type": "application/json"},
    )
    assert response.status == "400 BAD REQUEST"
    assert response.get_json() == {"message": {"size": "Number of records per page"}}


def test_successfully_retrieve_ad(client, ad):
    """Successfully retrieves an ad"""
    response = client.get(
        f"/ads/{ad.uuid}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status == "200 OK"
    assert response.get_json() == {
        "uuid": str(ad.uuid),
        "title": ad.title,
        "description": ad.description,
    }


def test_fails_retrieve_unexistent_resource(session, random_uuid, client):
    """Fails to retrieve a resource that does not exist"""
    response = client.get(
        f"/ads/{random_uuid}",
        headers={"Content-Type": "application/json"},
    )
    assert response.status == "404 NOT FOUND"
    assert response.get_json() == {
        "message": "The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again."
    }


@pytest.mark.parametrize("pk", (None, "-1", "1"))
def test_fails_to_retrieve_bad_id(client, pk):
    """Fails to retrieve a resource"""
    response = client.get(
        f"/ads/{pk}",
        headers={"Content-Type": "application/json"},
    )

    assert response.status == "404 NOT FOUND"
    assert response.get_json() is None
