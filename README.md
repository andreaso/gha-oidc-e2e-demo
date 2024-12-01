# GitHub Actions OIDC end-to-end demo

This is about [GitHub Actions' OIDC support][1]. In short it allows
you to authenticate your GitHub Actions jobs towards various cloud
providers using OIDC, rather than relying on long-lived service
account credentials.

To make it a bit more clear what's happening under the hood I put
together an end-to-end demo workflow.

* [oidc-auth-e2e-demo.yaml](.github/workflows/oidc-auth-e2e-demo.yaml)

That demo workflow is split into two parts. It starts off by showing
what actually happens inside the GitHub Actions job without relying on
the usual abstractions. Then the workflow continues with an extremely
simplified simulation of what conceptually happens at the cloud
provider's side.


## Usage

Hopefully simply reading the
[oidc-auth-e2e-demo.yaml](.github/workflows/oidc-auth-e2e-demo.yaml)
demo workflow and the
[verify_oidc_jwt.py](.github/helpers/verify_oidc_jwt.py) helper script
will provide a bit of helpful extra context.

Yet in case you decide to clone the repository to be able to muck
around a bit yourself do note that you'll need to modify the
`THAT_CLOUD_CONF_GH_ALLOWED_REPO` environment variable. At least
assuming that you want to be starting off in a passing state.


[1]: https://docs.github.com/en/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect
