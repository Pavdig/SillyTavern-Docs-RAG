
# Single Sign-On (SSO)

SSO allows you to create users and secure many different pages using a login portal presented on sites you want to secure. While it is complex to setup, it is a good way to both learn SSO and secure your ST instance out on the internet more.

SSO can also replace [HTTP Basic Authentication](SillyTavern_Administration_config-yaml.md) as an access control mechanism for [remote connections](SillyTavern_Administration_remote-connections.md).

This is recommended because SSO provides better security and functionality than HTTP Basic Authentication.

**Authelia** (https://www.authelia.com/) and **Authentik** (https://goauthentik.io/) are open-source SSO providers that can be used with SillyTavern.

## Sign in with SSO

If your SSO-provided username **exactly** matches the user handle of a SillyTavern user account, you can sign in to SillyTavern as that user by SSO. To enable this feature, change one of the following options to your [config.yaml](SillyTavern_Administration_config-yaml.md) file:

### Authelia

```yaml
sso:
  autheliaAuth: true
```

### Authentik

```yaml
sso:
  authentikAuth: true
```

Both options augment or replace the built-in [password management](SillyTavern_Usage_User_Settings_index.md) component of a [multi-user mode](SillyTavern_Administration_multi-user.md) setup.
