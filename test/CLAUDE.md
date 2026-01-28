# Test Guidelines

Context for Claude Code when working in `test/`.

## Test Strategy

| Type | Scope | Method |
|------|-------|--------|
| Unit | Individual section generators | pytest |
| Integration | Full document generation | Sample configs |
| Visual | Printed output inspection | `print_store_samples/` |
| Regression | Cross-version comparison | Diff generated docs |

## Conventions

- Test files: `test_<module>.py`
- Test functions: `test_<function>_<scenario>()`
- Use pytest fixtures for document/config setup
- Mock external services (no real file I/O in unit tests)

## Visual Testing

Store sample outputs in `print_store_samples/` for manual inspection:
- Print to physical paper (duplex)
- Verify recto/verso alignment
- Check page number positioning
- Confirm table dimensions

## Multi-Year Testing

Generator should produce stable output for any year. Test with:
- 2024 (leap year)
- 2025 (53-week year per ISO 8601)
- 2026 (standard year)
- 2027 (verification)
