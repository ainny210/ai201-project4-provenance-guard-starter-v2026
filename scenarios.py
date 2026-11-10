"""
Provenance Guard - Unit 8, Milestone 3

Evaluation scenarios for the five original acceptance criteria.

Criterion 1: False positives on 10 personally written human samples.
Criterion 2: AI vs human confidence score spread.
Criterion 3: Coverage of all three classification labels.
Criterion 4: Appeal workflow (tested separately).
Criterion 5: Invalid input handling.


"""

# ---------------------------------------------------------
# SAMPLE DATA
# ---------------------------------------------------------


HUMAN_SAMPLES = [
    "Yesterday i was working on my thesis project of my masters so i spent more time on organizaing vulnerablity data and checking whether graphs result numbers are consistent across the years than writing the thesis.",

    "I had problem understanding one of the codepath assignments at first after reviewing the examples and datsets and trying the problem again i started to understand the solutions.",

    "My Laptop was running slowly when I opened a multiple excel file simulataneously i tried closing other applications and filtering the data still took longer than expected.",

    "In my new job i attend a meetings where we discussed how organizations should monitor new security vulnerabilities i learned that identifying affected systems is an important part of responding to security alerts also making backups.",

    "I was testing a Python application and noticed that some requests were failing i checked the server audit logs and realized I needed to verify whether the application server was actually running or not.",

    "Last week I reviewed many database security vulnerablities and some vulnerabilities were related to authentication while others involved access control or improper input validation.",

    "In my opinion testing is an important part of as SDLC part because applications sometimes behave differently than expected,so running same test multiple times can help identify inconsistent results or abnormalities in application.",

    "During my Masters thesis research i created charts/graphs to compare vulnerabilities across database systems, charts made it easier to understand which products had more reported security issues.",

    "I was learning about AI security in terms of policies GRC part and how organizations can protect their systems from malicious prompts or inputs and i found one that AI applications require different types of testing.",

    "From Last two days even today i working on flask application as i enabled rate limit testing several requests and checked their audit log to confirm that rejected submission were saved and recorded.",

]

# AI-generated examples for comparison.
AI_SAMPLES = [
    "Artificial intelligence has fundamentally transformed modern computing by enabling organizations to automate complex workflows, optimize operational efficiency, and derive actionable insights from large datasets.",

    "Cybersecurity represents a critical component of modern digital infrastructure. Organizations must implement comprehensive security controls to protect sensitive information and maintain operational resilience.",

    "Machine learning algorithms identify patterns within structured and unstructured datasets, enabling predictive analysis and supporting data-driven decision-making across diverse industries.",

    "Database management systems provide essential mechanisms for storing, retrieving, and organizing information while ensuring data integrity, availability, and controlled access.",

    "Effective risk management requires a systematic approach to identifying potential threats, evaluating their likelihood and impact, and implementing appropriate mitigation strategies.",

    "The integration of artificial intelligence into enterprise environments introduces significant opportunities for innovation while simultaneously creating new security and governance challenges.",

    "Organizations should establish robust monitoring procedures, implement layered defensive controls, and continuously evaluate their cybersecurity posture against emerging threats.",

    "Natural language processing enables computational systems to interpret, analyze, and generate human language through statistical modeling and advanced neural network architectures.",

    "Software quality assurance involves systematic testing methodologies designed to identify defects, validate functional requirements, and improve the reliability of applications.",

    "Responsible artificial intelligence development requires transparency, accountability, fairness, and continuous assessment of potential risks throughout the system lifecycle.",
]

# Additional varied samples for classification coverage.
BORDERLINE_SAMPLES = [
    "I think AI is useful, but sometimes it gives answers that sound correct even when they are wrong.",

    "The system processed the request successfully. However, the resulting classification did not match the expected output.",

    "Today was busy. I worked on my assignment, attended a meeting, and fixed a problem in my code.",

    "Artificial intelligence can support productivity, although human review remains important for high-risk decisions.",

    "I opened the application and tried submitting the same text twice. The scores were slightly different.",

    "Security testing helps teams find problems before attackers exploit them.",

    "The experiment evaluated multiple samples to determine whether the classification thresholds were appropriate.",

    "My first attempt failed because the server was not responding. I restarted it and tried again.",

    "Automated systems can improve consistency, but their outputs still require careful validation.",

    "I spent an hour debugging a Python script. The problem turned out to be a small configuration issue.",
]


# ---------------------------------------------------------
# EVALUATION SCENARIOS
# ---------------------------------------------------------

SCENARIOS = [
    {
        "name": "false positive diagnostic placeholders",
        "criterion": 1,
        "texts": HUMAN_SAMPLES,
    },

    {
        "name": "AI confidence score spread",
        "criterion": 2,
        "texts": AI_SAMPLES,
    },

    {
        "name": "human confidence score spread placeholders",
        "criterion": 2,
        "texts": HUMAN_SAMPLES,
    },

    {
        "name": "label coverage",
        "criterion": 3,
        "texts": HUMAN_SAMPLES + AI_SAMPLES + BORDERLINE_SAMPLES,
    },

    {
        "name": "bad input handling",
        "criterion": 5,
        "bodies": [
            {"text": "", "creator_id": "eval_bad_01"},
            {"creator_id": "eval_bad_02"},
            {"text": None, "creator_id": "eval_bad_03"},
            {"text": 12345, "creator_id": "eval_bad_04"},
            {"text": [], "creator_id": "eval_bad_05"},
            {"text": {}, "creator_id": "eval_bad_06"},
            {"text": True, "creator_id": "eval_bad_07"},
            {"text": "   ", "creator_id": "eval_bad_08"},
            {"text": "word " * 50000, "creator_id": "eval_bad_09"},
            {"text": ["hello", "world"], "creator_id": "eval_bad_10"},
        ],
    },
]


# ---------------------------------------------------------
# VALIDATION
# ---------------------------------------------------------

def validate() -> list[str]:
    """
    Validate scenario structure before running evaluation.
    """

    problems = []

    for i, scenario in enumerate(SCENARIOS, 1):

        if not scenario.get("name"):
            problems.append(f"scenario {i} has no name")

        texts = scenario.get("texts")
        bodies = scenario.get("bodies")

        if texts and bodies:
            problems.append(
                f"scenario {i} ('{scenario.get('name')}') "
                f"has both texts and bodies"
            )
            continue

        if bodies:
            for j, body in enumerate(bodies, 1):
                if not isinstance(body, dict):
                    problems.append(
                        f"scenario {i}, body {j} is not a dict"
                    )
            continue

        if not texts:
            problems.append(
                f"scenario {i} has no texts and no bodies"
            )
            continue

        for j, sample in enumerate(texts, 1):

            if not isinstance(sample, str) or not sample.strip():
                problems.append(
                    f"scenario {i}, text {j} is empty or invalid"
                )

            elif sample.startswith("REPLACE ME"):
                problems.append(
                    f"scenario {i}, text {j} is still a placeholder"
                )

    return problems