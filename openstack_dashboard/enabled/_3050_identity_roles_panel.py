# The slug of the panel to be added to HORIZON_CONFIG. Required.
PANEL = 'roles'
# The slug of the dashboard the PANEL associated with. Required.
PANEL_GROUP = 'default'
# The slug of the panel group the PANEL is associated with.
PANEL_DASHBOARD = 'identity'

# Python panel class of the PANEL to be added.
# ADD_PANEL = 'openstack_dashboard.dashboards.identity.roles.panel.Roles'
ADD_PANEL = 'openstack_dashboard.contrib.identity.roles.panel.Roles'
