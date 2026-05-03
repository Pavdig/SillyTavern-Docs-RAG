# Single Sign-On (SSO)

Despite all the benefits of SSO, it is a complex system to set up and maintain. If not configured correctly, it can lead to unauthorized access to your instance. Make sure to properly configure and test your setup before enabling SSO. If you are unsure about the security implications, it is recommended to keep SSO auto-login disabled and resort to other authentication methods instead.
SSO allows you to create users and secure many different pages using a login portal presented on sites you want to secure. While it is complex to setup, it is a good way to both learn SSO and secure your ST instance out on the internet more.

SSO can also replace [HTTP Basic Authentication](SillyTavern_Administration_config-yaml.md) as an access control mechanism for [remote connections](SillyTavern_Administration_remote-connections.md).

This is recommended because SSO provides better security and functionality than HTTP Basic Authentication.

**Authelia** (https://www.authelia.com/) and **Authentik** (https://goauthentik.io/) are open-source SSO providers that can be used with SillyTavern.

## Configure trusted proxies

Only requests from IP addresses that are configured as trusted proxies will be able to authenticate users by forwarding the necessary headers. By default, both IPv4 and IPv6 loopback addresses are trusted. To allow other IPs to authenticate with SSO headers, add them to the `sso.trustedProxies` list in your [config.yaml](SillyTavern_Administration_config-yaml.md) file:

Also supports CIDR and wildcard notation for specifying multiple IPs or ranges, e.g., `192.168.0.*` or `10.0.0.0/24`.
```yaml
sso:
  trustedProxies:
    - ::1           # IPv6 loopback address - trusted by default
    - 127.0.0.1     # IPv4 loopback address - trusted by default
    - '192.168.0.1' # Example IP address of a trusted proxy
```

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
