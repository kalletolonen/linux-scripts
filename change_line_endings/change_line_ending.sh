/bin/bash -c 'sed "s/\r//" < "/c/Users/kalle.tolonen/ratko/ratko-ui-backend/src/docker/postgis/restore/restore_full.sh" > "/c/Users/kalle.tolonen/ratko/ratko-ui-backend/src/docker/postgis/restore/restore_full_unix.sh" \
    && chmod 777 "/c/Users/kalle.tolonen/ratko/ratko-ui-backend/src/docker/postgis/restore/restore_full_unix.sh" \
    && mv "/c/Users/kalle.tolonen/ratko/ratko-ui-backend/src/docker/postgis/restore/restore_full_unix.sh" "/c/Users/kalle.tolonen/ratko/ratko-ui-backend/src/docker/postgis/restore/restore_full.sh"'
