---
name: copilot-instructions-blueprint-generator
description: 'Technology-agnostic blueprint generator for creating comprehensive copilot-instructions.md files that guide GitHub Copilot to produce code consistent with project standards, architecture patterns, and exact technology versions by analyzing existing codebase patterns and avoiding assumptions.'
---

# Copilot Instructions Blueprint Generator

## Configuration Variables
${PROJECT_TYPE="Java|JavaScript|TypeScript|React|Angular|Python|GO|bash|Multiple|Other"} <!-- Primary technology -->
${ARCHITECTURE_STYLE="Layered|Microservices|Monolithic|Domain-Driven|Event-Driven|Serverless|Mixed"} <!-- Architectural approach -->
${CODE_QUALITY_FOCUS="Maintainability|Performance|Security|Accessibility|Testability|All"} <!-- Quality priorities -->
${DOCUMENTATION_LEVEL="Minimal|Standard|Comprehensive"} <!-- Documentation requirements -->
${TESTING_REQUIREMENTS="Unit|Integration|E2E|TDD|BDD|All"} <!-- Testing approach -->
${VERSIONING="Semantic|CalVer|Custom"} <!-- Versioning approach -->

## Generated Prompt

"Generate a comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code consistent with our project's standards, architecture, and technology versions. The instructions must be strictly based on actual code patterns in our codebase and avoid making any assumptions. Follow this approach:

### 1. Core Instruction Structure

```markdown
# GitHub Copilot Instructions

## Priority Guidelines

When generating code for this repository:

1. **Version Compatibility**: Always detect and respect the exact versions of languages, frameworks, and libraries used in this project
2. **Context Files**: Prioritize patterns and standards defined in the .github/copilot directory
3. **Codebase Patterns**: When context files don't provide specific guidance, scan the codebase for established patterns
4. **Architectural Consistency**: Maintain our ${ARCHITECTURE_STYLE} architectural style and established boundaries
5. **Code Quality**: If CODE_QUALITY_FOCUS is set to "All", include all quality focuses; otherwise, use the specified CODE_QUALITY_FOCUS.

## Technology Version Detection

Before generating code, scan the codebase to identify:

1. **Language Versions**: Detect the exact versions of programming languages in use
   - Examine project files, configuration files, and package managers
   - Look for language-specific version indicators in project and configuration files
   - Never use language features beyond the detected version

2. **Framework Versions**: Identify the exact versions of all frameworks
   - Check package.json, pom.xml, requirements.txt, go.mod, and other relevant project files
   - Respect version constraints when generating code
   - Never suggest features not available in the detected framework versions

3. **Library Versions**: Note the exact versions of key libraries and dependencies
   - Generate code compatible with these specific versions
   - Never use APIs or features not available in the detected versions

## Context Files

Prioritize the following files in .github/copilot directory (if they exist):

- **architecture.md**: System architecture guidelines
- **tech-stack.md**: Technology versions and framework details
- **coding-standards.md**: Code style and formatting standards
- **folder-structure.md**: Project organization guidelines
- **exemplars.md**: Exemplary code patterns to follow

## Codebase Scanning Instructions

When context files don't provide specific guidance:

1. Identify similar files to the one being modified or created
2. Analyze patterns for:
   - Naming conventions
   - Code organization
   - Error handling
   - Logging approaches
   - Documentation style
   - Testing patterns
   
3. Follow the most consistent patterns found in the codebase
4. When conflicting patterns exist, prioritize patterns in newer files or files with higher test coverage
5. Never introduce patterns not found in the existing codebase

## Code Quality Standards

### Maintainability (when CODE_QUALITY_FOCUS is "Maintainability" or "All")
- Write self-documenting code with clear naming
- Follow the naming and organization conventions evident in the codebase
- Follow established patterns for consistency
- Keep functions focused on single responsibilities
- Limit function complexity and length to match existing patterns

### Performance (when CODE_QUALITY_FOCUS is "Performance" or "All")
- Follow existing patterns for memory and resource management
- Match existing patterns for handling computationally expensive operations
- Follow established patterns for asynchronous operations
- Apply caching consistently with existing patterns
- Optimize according to patterns evident in the codebase

### Security (when CODE_QUALITY_FOCUS is "Security" or "All")
- Follow existing patterns for input validation
- Apply the same sanitization techniques used in the codebase
- Use parameterized queries matching existing patterns
- Follow established authentication and authorization patterns
- Handle sensitive data according to existing patterns

### Accessibility (when CODE_QUALITY_FOCUS is "Accessibility" or "All")
- Follow existing accessibility patterns in the codebase
- Match ARIA attribute usage with existing components
- Maintain keyboard navigation support consistent with existing code
- Follow established patterns for color and contrast
- Apply text alternative patterns consistent with the codebase

### Testability (when CODE_QUALITY_FOCUS is "Testability" or "All")
- Follow established patterns for testable code
- Match dependency injection approaches used in the codebase
- Apply the same patterns for managing dependencies
- Follow established mocking and test double patterns
- Match the testing style used in existing tests

## Documentation Requirements

### Minimal documentation (when DOCUMENTATION_LEVEL is "Minimal")
- Match the level and style of comments found in existing code
- Document according to patterns observed in the codebase
- Follow existing patterns for documenting non-obvious behavior
- Use the same format for parameter descriptions as existing code

### Standard documentation (when DOCUMENTATION_LEVEL is "Standard")
- Follow the exact documentation format found in the codebase
- Match the XML/JSDoc style and completeness of existing comments
- Document parameters, returns, and exceptions in the same style
- Follow existing patterns for usage examples
- Match class-level documentation style and content

### Comprehensive documentation (when DOCUMENTATION_LEVEL is "Comprehensive")
- Follow the most detailed documentation patterns found in the codebase
- Match the style and completeness of the best-documented code
- Document exactly as the most thoroughly documented files do
- Follow existing patterns for linking documentation
- Match the level of detail in explanations of design decisions

## Testing Approach

${TESTING_REQUIREMENTS.includes("Unit") || TESTING_REQUIREMENTS == "All" ? 
`### Unit Testing
- Match the exact structure and style of existing unit tests
- Follow the same naming conventions for test classes and methods
- Use the same assertion patterns found in existing tests
- Apply the same mocking approach used in the codebase
- Follow existing patterns for test isolation` : ""}

${TESTING_REQUIREMENTS.includes("Integration") || TESTING_REQUIREMENTS == "All" ? 
`### Integration Testing
- Follow the same integration test patterns found in the codebase
- Match existing patterns for test data setup and teardown
- Use the same approach for testing component interactions
- Follow existing patterns for verifying system behavior` : ""}

${TESTING_REQUIREMENTS.includes("E2E") || TESTING_REQUIREMENTS == "All" ? 
`### End-to-End Testing
- Match the existing E2E test structure and patterns
- Follow established patterns for UI testing
- Apply the same approach for verifying user journeys` : ""}

${TESTING_REQUIREMENTS.includes("TDD") || TESTING_REQUIREMENTS == "All" ? 
`### Test-Driven Development
- Follow TDD patterns evident in the codebase
- Match the progression of test cases seen in existing code
- Apply the same refactoring patterns after tests pass` : ""}

${TESTING_REQUIREMENTS.includes("BDD") || TESTING_REQUIREMENTS == "All" ? 
`### Behavior-Driven Development
- Match the existing Given-When-Then structure in tests
- Follow the same patterns for behavior descriptions
- Apply the same level of business focus in test cases` : ""}

## Technology-Specific Guidelines

${PROJECT_TYPE == "Java" || PROJECT_TYPE == "Multiple" ? `### Java Guidelines
- Detect and adhere to the specific Java version in use
- Follow the exact same design patterns found in the codebase
- Match exception handling patterns from existing code
- Use the same collection types and approaches found in the codebase
- Apply the dependency injection patterns evident in existing code` : ""}

${PROJECT_TYPE == "JavaScript" || PROJECT_TYPE == "TypeScript" || PROJECT_TYPE == "Multiple" ? `### JavaScript/TypeScript Guidelines
- Detect and adhere to the specific ECMAScript/TypeScript version in use
- Follow the same module import/export patterns found in the codebase
- Match TypeScript type definitions with existing patterns
- Use the same async patterns (promises, async/await) as existing code
- Follow error handling patterns from similar files` : ""}

${PROJECT_TYPE == "React" || PROJECT_TYPE == "Multiple" ? `### React Guidelines
- Detect and adhere to the specific React version in use
- Match component structure patterns from existing components
- Follow the same hooks and lifecycle patterns found in the codebase
- Apply the same state management approach used in existing components
- Match prop typing and validation patterns from existing code` : ""}

${PROJECT_TYPE == "Angular" || PROJECT_TYPE == "Multiple" ? `### Angular Guidelines
- Detect and adhere to the specific Angular version in use
- Follow the same component and module patterns found in the codebase
- Match decorator usage exactly as seen in existing code
- Apply the same RxJS patterns found in the codebase
- Follow existing patterns for component communication` : ""}

${PROJECT_TYPE == "Python" || PROJECT_TYPE == "Multiple" ? `### Python Guidelines
- Detect and adhere to the specific Python version in use
- Follow the same import organization found in existing modules
- Match type hinting approaches if used in the codebase
- Apply the same error handling patterns found in existing code
- Follow the same module organization patterns` : ""}

${PROJECT_TYPE == "GO" || PROJECT_TYPE == "Multiple" ? `### Go Guidelines
- Detect and adhere to the specific Go version in use
- Follow package, naming, and error handling patterns found in the codebase
- Match established approaches for concurrency and resource management
- Use the same testing and formatting conventions as existing Go code` : ""}

${PROJECT_TYPE == "bash" || PROJECT_TYPE == "Multiple" ? `### Bash Guidelines
- Detect and adhere to the Bash version and shell compatibility requirements in use
- Follow existing patterns for quoting, argument handling, and exit status checks
- Match established conventions for portability, logging, and cleanup
- Use the same testing and validation patterns as existing shell scripts` : ""}

## Version Control Guidelines

${VERSIONING == "Semantic" ? 
`- Follow Semantic Versioning patterns as applied in the codebase
- Match existing patterns for documenting breaking changes
- Follow the same approach for deprecation notices` : ""}

${VERSIONING == "CalVer" ? 
`- Follow Calendar Versioning patterns as applied in the codebase
- Match existing patterns for documenting changes
- Follow the same approach for highlighting significant changes` : ""}

${VERSIONING == "Custom" ? 
`- Match the exact versioning pattern observed in the codebase
- Follow the same changelog format used in existing documentation
- Apply the same tagging conventions used in the project` : ""}

## General Best Practices

- Follow naming conventions exactly as they appear in existing code
- Match code organization patterns from similar files
- Apply error handling consistent with existing patterns
- Follow the same approach to testing as seen in the codebase
- Match logging patterns from existing code
- Use the same approach to configuration as seen in the codebase

## Prompt and Decision Memory

- Keep project memory under `.github/copilot/`, alongside the generated instructions
- Record prompts introduced or substantially changed in `.github/copilot/prompt-history.md`
- Record important implementation or configuration decisions in `.github/copilot/decisions/`
- For every recorded decision, include its justification, affected files or areas, date, and status
- Update the memory record when a decision changes, and preserve the previous rationale for traceability
- Consult the memory record before making related changes so prior decisions remain consistent

## Project-Specific Guidance

- Scan the codebase thoroughly before generating any code
- Respect existing architectural boundaries without exception
- Match the style and patterns of surrounding code
- Update the repository's global README when adding or changing a reusable asset, repository convention, supported technology, or user-facing workflow
- Keep the README structure and examples consistent with the current repository contents
- When in doubt, prioritize consistency with existing code over external best practices
```

### 2. Codebase Analysis Instructions

To create the copilot-instructions.md file, first analyze the codebase to:

1. **Identify Exact Technology Versions**:
   - Focus on ${PROJECT_TYPE} technologies
   - Extract precise version information from project files, package.json, and other relevant configuration files
   - Document version constraints and compatibility requirements

2. **Understand Architecture**:
   - Analyze folder structure and module organization
   - Identify clear layer boundaries and component relationships
   - Document communication patterns between components

3. **Document Code Patterns**:
   - Catalog naming conventions for different code elements
   - Note documentation styles and completeness
   - Document error handling patterns
   - Map testing approaches and coverage

4. **Note Quality Standards**:
   - Identify performance optimization techniques actually used
   - Document security practices implemented in the code
   - Note accessibility features present (if applicable)
   - Document code quality patterns evident in the codebase

5. **Maintain Prompt and Decision Memory**:
   - Record new prompts and substantial prompt changes
   - Record important decisions together with their justifications
   - Preserve enough context for future contributors to understand and revisit those decisions

### 3. Implementation Notes

The final copilot-instructions.md should:
- Be placed in the .github/copilot directory
- Include or link to `.github/copilot/prompt-history.md` and `.github/copilot/decisions/`
- Require an update to the repository's global README when the generated change affects repository structure, reusable assets, supported technologies, conventions, or user-facing workflows
- Reference only patterns and standards that exist in the codebase
- Include explicit version compatibility requirements
- Avoid prescribing any practices not evident in the code
- Provide concrete examples from the codebase
- Be comprehensive yet concise enough for Copilot to effectively use

Important: Only include guidance based on patterns actually observed in the codebase. Explicitly instruct Copilot to prioritize consistency with existing code over external best practices or newer language features.
"

## Expected Output

A comprehensive copilot-instructions.md file that will guide GitHub Copilot to produce code that is perfectly compatible with your existing technology versions and follows your established patterns and architecture.
