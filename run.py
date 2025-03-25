# This page runs the actual application and needs to be built out with the -
# if __name__ == "__main__":
#     app.run(
#         host=os.environ.get("IP"),
#         port=int(os.environ.get("PORT")),
#         debug=os.environ.get("DEBUG")
#     )

import os
from taskmanager import app


if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP"),
        port=int(os.environ.get("PORT")),
        debug=os.environ.get("DEBUG"),
    )
