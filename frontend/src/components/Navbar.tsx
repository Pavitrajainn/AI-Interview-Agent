export default function Navbar() {
  return (
    <nav className="border-b bg-white">
      <div className="mx-auto flex max-w-7xl items-center justify-between px-6 py-4">

        {/* Logo */}
        <div className="text-xl font-bold">
          AI Interview Agent
        </div>

        {/* Navigation */}
        <div className="hidden items-center gap-8 md:flex">
          <a
            href="#features"
            className="text-sm font-medium hover:text-gray-600"
          >
            Features
          </a>

          <a
            href="#about"
            className="text-sm font-medium hover:text-gray-600"
          >
            About
          </a>

          <button className="rounded-md bg-black px-4 py-2 text-sm font-medium text-white hover:bg-gray-800">
            Start Interview
          </button>
        </div>

      </div>
    </nav>
  );
}