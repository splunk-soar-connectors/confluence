**Unreleased**

* Existing assets must be reviewed after upgrade: the secure default applies when no certificate-verification value is stored, but a persisted disabled value is preserved because it cannot be distinguished from an intentional administrator opt-out. Set **Verify server TLS certificate** to enabled and save each existing asset unless an explicit exception is required.
