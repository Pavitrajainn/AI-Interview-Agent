const features = [
  {
    title: "Adaptive Questions",
    description:
      "AI dynamically adjusts interview questions based on your answers and skill level.",
    icon: "🎯",
  },
  {
    title: "Answer Analysis",
    description:
      "Get AI-powered analysis of your answers, including strengths and areas to improve.",
    icon: "🧠",
  },
  {
    title: "Personalized Feedback",
    description:
      "Receive detailed feedback and actionable suggestions after your interview.",
    icon: "💡",
  },
  {
    title: "Performance Report",
    description:
      "Track your interview performance and understand where you need improvement.",
    icon: "📊",
  },
];

export default function Features() {
  return (
    <section id="features" className="bg-gray-50 py-20">
      <div className="mx-auto max-w-7xl px-6">

        {/* Heading */}
        <div className="mx-auto max-w-2xl text-center">
          <h2 className="text-3xl font-bold text-gray-900 md:text-4xl">
            Everything You Need to Ace Your Interview
          </h2>

          <p className="mt-4 text-gray-600">
            Our AI-powered platform helps you practice, analyze, and improve
            your interview skills.
          </p>
        </div>

        {/* Cards */}
        <div className="mt-12 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => (
            <div
              key={feature.title}
              className="rounded-xl border bg-white p-6 shadow-sm transition hover:-translate-y-1 hover:shadow-md"
            >
              <div className="text-3xl">
                {feature.icon}
              </div>

              <h3 className="mt-4 text-lg font-semibold text-gray-900">
                {feature.title}
              </h3>

              <p className="mt-2 text-sm leading-6 text-gray-600">
                {feature.description}
              </p>
            </div>
          ))}
        </div>

      </div>
    </section>
  );
}