from flask import Flask, jsonify


app = Flask(__name__)

PROFILE = {
    "name": "Becker",
    "role": "Junior Full Stack Developer",
    "location": "Sao Paulo, Brazil",
    "focus": "Landing pages, dashboards, APIs, and SaaS interfaces",
}

PROJECTS = [
    {
        "slug": "portfolio-landing-premium",
        "name": "Premium Portfolio Landing",
        "type": "Frontend showcase",
        "stack": ["HTML", "CSS", "JavaScript"],
    },
    {
        "slug": "crm-comercial-fullstack",
        "name": "Commercial CRM Demo",
        "type": "Full stack product demo",
        "stack": ["React", "Node.js", "MongoDB"],
    },
    {
        "slug": "saas-auth-dashboard-demo",
        "name": "SaaS Auth Dashboard Demo",
        "type": "Authentication workspace",
        "stack": ["React", "Node.js", "JWT"],
    },
]


@app.get("/")
def root():
    return jsonify(
        {
            "service": "portfolio-api-python",
            "status": "online",
            "version": "1.0.0",
            "routes": [
                "/health",
                "/api/profile",
                "/api/projects",
                "/api/stack",
            ],
        }
    )


@app.get("/health")
def health():
    return jsonify({"status": "ok"})


@app.get("/api/profile")
def profile():
    return jsonify(PROFILE)


@app.get("/api/projects")
def projects():
    return jsonify({"items": PROJECTS, "total": len(PROJECTS)})


@app.get("/api/stack")
def stack():
    stack_items = sorted({item for project in PROJECTS for item in project["stack"]})
    return jsonify({"items": stack_items})


if __name__ == "__main__":
    app.run(debug=True)
