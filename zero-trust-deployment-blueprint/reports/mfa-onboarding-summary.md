# MFA Device Onboarding Summary

## Objective

Configured SSH authentication to support Time-Based One-Time Password MFA using the Google Authenticator PAM module.

## Policy

SSH access now requires PAM-based interactive authentication. The MFA secret file was generated for the Ubuntu user and a redacted copy was saved for documentation purposes.

## Security Notes

The live MFA secret must never be committed to GitHub. Only the redacted validation copy should be stored in the project repository.
