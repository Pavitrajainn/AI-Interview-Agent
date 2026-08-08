export default function Hero() {
  return (
    <section className="min-h-[80vh] bg-white">
      <div className="mx-auto flex max-w-7xl flex-col items-center px-6 py-24 text-center">

        {/* Badge */}
        <div className="mb-6 rounded-full border bg-gray-50 px-4 py-2 text-sm text-gray-600">
          🤖 AI-Powered Interview Platform
        </div>

        {/* Heading */}
        <h1 className="max-w-4xl text-4xl font-bold tracking-tight text-gray-900 md:text-6xl">
          Practice Interviews with
          <span className="block text-gray-600">
            Your AI Interview Agent
          </span>
        </h1>

        {/* Description */}
        <p className="mt-6 max-w-2xl text-lg leading-8 text-gray-600">
          Experience realistic AI-powered interviews that adapt to your
          skills, analyze your answers, and provide personalized feedback
          to help you improve.
        </p>

        {/* Buttons */}
        <div className="mt-8 flex flex-col gap-4 sm:flex-row">

          <button className="rounded-md bg-black px-6 py-3 font-medium text-white hover:bg-gray-800">
            Start Interview →
          </button>

          <button className="rounded-md border px-6 py-3 font-medium text-gray-700 hover:bg-gray-50">
            Learn More
          </button>

        </div>

      </div>
    </section>
  );
}