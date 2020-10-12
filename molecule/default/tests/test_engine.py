def test_nginx_is_enabled(host):
    assert host.service("nginx").is_enabled


def test_ngix_is_running(host):
    assert host.service("nginx").is_running
