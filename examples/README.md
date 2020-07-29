In this folder several example notebooks are shown. To run these locally make sure you 
install [jupyter](https://jupyter.org/install) and the threedi-openapi-client:
    
    pip3 install threedi-api-client notebook

To run the advanced notebooks you'll also need the following packages:
    
    pip3 install ipyleaflet websockets


If you are new to the threedi-api, we recommend walking through the notebook examples  
in the following order:

Basics:
- [starting your first simulation](./starting_your_first_simulation.ipynb)
- [adding events to a simulation](./simulation_with_events.ipynb)
- [download simulation results](./download_simulation_results.ipynb)

Advanced
- [visualise a threedimodel](./visualise_threedimodel.ipynb)
- [interact with simulations via websockets](./interact_via_websocket.ipynb)

These notebooks only show the tip of the iceberg of what's possible with the 3Di api, but 
should give you an understanding of how to use the api-client. Go to https://api.3di.live/v3.0/swagger/ 
to see the complete api.
