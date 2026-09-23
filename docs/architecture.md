## 1. Core Architectural Rules
* **Code Style:** Prefer functional programming patterns, immutability, and explicit type definitions over implicit ones.
* **File Structure:** Maintain strict separation of concerns. Follow the established directory layout:
  * `/components` -> Pure UI components only (no direct data fetching).
  * `/hooks` -> Reusable custom hooks handling state and logic.
  * `/app` -> Next.js routing, pages, and Server Actions.
* **State Management:** Use server state and URL params wherever possible. Avoid global client-side state unless strictly necessary.