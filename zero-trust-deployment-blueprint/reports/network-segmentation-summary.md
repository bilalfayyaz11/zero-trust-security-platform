# Zero Trust Network Segmentation Summary

## Segmentation Model

This environment simulates two security zones:

- Sensitive Zone: 192.168.1.0/24
- General User Zone: 192.168.2.0/24

## Policies Implemented

- Cross-zone forwarding traffic is rejected.
- Same-zone source traffic is accepted.
- Web application access on port 8080 is restricted to a specific trusted IP.
- Database access on port 3306 is blocked from the general user zone.

## Implementation Notes

The lab originally suggested using the INPUT chain for blocking traffic between network zones. This was corrected by using the FORWARD chain for inter-zone segmentation because INPUT only applies to traffic destined for the local host.
