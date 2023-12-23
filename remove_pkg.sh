curl --request DELETE --header "PRIVATE-TOKEN: $INBOC_DEV_PYPI_TOKEN" "https://gitlab.inboc.net/api/v4/projects/93/packages/$(curl -s --header "PRIVATE-TOKEN: $INBOC_DEV_PYPI_TOKEN" "https://gitlab.inboc.net/api/v4/projects/93/packages?per_page=100" | json_pp | grep -B 2 $PACKAGE_NAME | grep id | awk '{print $3}' | awk -F',' '{print $1}')"

