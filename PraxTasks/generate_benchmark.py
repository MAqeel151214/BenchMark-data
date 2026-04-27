import json
from datetime import datetime, timezone, timedelta

benchmark = {
    "benchmark": "TAVS",
    "version": "1.0",
    "session_metadata": {
        "session_id": "S-PRAX-06B",
        "generator_model": "claude-opus-4",
        "category": "PRAXIS",
        "subcategory": "Scientific Research — Experimental Design, Controls, Bias Mitigation, Statistical Power",
        "generated_at": "2026-04-25T13:13:53+05:00"
    },
    "tasks": [
        {
            "task_id": "S-PRAX-06B-001",
            "category": "PRAXIS",
            "subcategory": "Statistical power and sample size",
            "bloom_level": "Apply",
            "difficulty_tier": "Medium",
            "difficulty_score": 5,
            "prompt": "A pharmaceutical company is developing Drug X to reduce systolic blood pressure (SBP). A Phase II pilot study suggests Drug X reduces SBP by an average of δ = 8 mmHg more than the current standard of care. The pooled standard deviation from the pilot is σ = 15 mmHg. The company plans a two-arm randomized controlled trial with 1:1 allocation (Drug X versus Standard). They want to detect this specific effect size with 90% statistical power at a two-sided significance level of α = 0.05.\n\nUsing the standard formula for the per-group sample size in a two-sample t-test with equal variances:\n\nn = (Z_{α/2} + Z_β)² × 2σ² / δ²\n\nwhere Z_{α/2} is the critical value for the two-sided test and Z_β is the critical value corresponding to the desired power. Use Z_{0.025} = 1.96 and Z_{0.10} = 1.28.\n\nCompute the minimum required sample size per group. Show your calculation steps explicitly, and state whether you rounded up or down and why.",
            "prompt_format": "open_ended",
            "constraints": [
                "Show all calculation steps explicitly",
                "Final answer must be a single integer representing the per-group sample size"
            ],
            "ground_truth": {
                "answer": "74",
                "answer_type": "exact_integer",
                "tolerance": None,
                "solution_steps": [
                    "Step 1: Substitute the given values into the formula: Z_{α/2} = 1.96, Z_β = 1.28, σ = 15, δ = 8.",
                    "Step 2: Compute the sum of Z-values: 1.96 + 1.28 = 3.24.",
                    "Step 3: Square the sum: 3.24² = 10.4976.",
                    "Step 4: Compute 2σ²: 2 × 15² = 2 × 225 = 450.",
                    "Step 5: Multiply: 10.4976 × 450 = 4723.92.",
                    "Step 6: Divide by δ² = 64: 4723.92 / 64 = 73.81125.",
                    "Step 7: Round UP to the next integer because sample size must be a whole number and rounding down would yield power strictly less than 90%. The minimum required sample size is 74 per group."
                ],
                "verification_method": "numerical",
                "verification_code": "import math\nz_alpha = 1.96\nz_beta = 1.28\nsigma = 15\ndelta = 8\nn = (z_alpha + z_beta)**2 * 2 * sigma**2 / delta**2\nprint(math.ceil(n))  # Expected: 74"
            },
            "meta_reasoning": {
                "common_errors": [
                    "Rounding down to 73 instead of up, failing to recognize that rounding down reduces power below the target",
                    "Using the total sample size formula instead of per-group, yielding 148 and missing that the question asks for per-group n",
                    "Incorrectly using a one-tailed Z-value (1.645) instead of the two-tailed value (1.96)"
                ],
                "required_knowledge": [
                    "Two-sample t-test sample size formula",
                    "Relationship between alpha, beta, and sample size",
                    "Rounding conventions in sample size calculations"
                ],
                "reasoning_depth": 3,
                "estimated_human_time_minutes": 6
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["power-analysis", "sample-size-calculation", "clinical-trial-design", "two-sample-t-test"]
        },
        {
            "task_id": "S-PRAX-06B-002",
            "category": "PRAXIS",
            "subcategory": "Experimental design and confounder control",
            "bloom_level": "Analyze",
            "difficulty_tier": "Medium",
            "difficulty_score": 5,
            "prompt": "An ecologist wants to determine whether chronic anthropogenic noise from natural gas compressor stations reduces nesting success of the sagebrush sparrow (Artemisiospiza nevadensis). The three most important known confounders are: (1) habitat quality (vegetation density), (2) predator density (corvid abundance), and (3) weather conditions (spring rainfall).\n\nFour research teams propose different study designs:\n\n**Design A:** Compare nesting success at 15 sites located near compressor stations against 15 sites far from compressors. Sites are matched visually for habitat type, but predator density and weather are not measured.\n\n**Design B:** Compare nesting success at 15 compressor-proximate sites during the current breeding season with historical nesting success data from the same 15 sites collected 10 years ago (before compressors were installed).\n\n**Design C:** Measure nesting success at 30 sites spanning a continuous gradient of noise exposure (30–85 dB). Use multiple linear regression to statistically control for measured habitat quality, predator visit rates, and rainfall.\n\n**Design D:** Identify 15 pairs of sites with comparable habitat quality and predator density. Within each pair, randomly assign one site to receive a speaker broadcasting recorded compressor noise and the other to receive a silent speaker. Monitor nesting success over one breeding season while recording weather at all sites.\n\nWhich design most effectively isolates the causal effect of compressor noise on nesting success while controlling for the stated confounders? Select one letter and justify your choice.",
            "prompt_format": "multiple_choice",
            "constraints": [
                "Select exactly one option (A, B, C, or D)",
                "Provide a 2-3 sentence justification referencing specific confounders"
            ],
            "ground_truth": {
                "answer": "D",
                "answer_type": "multiple_choice_letter",
                "tolerance": None,
                "solution_steps": [
                    "Step 1: Design A is observational and confounded by predator density and weather, which vary across geographically separated sites and are not measured or controlled.",
                    "Step 2: Design B is a weak before-after design confounded by temporal trends, ecological changes over the 10-year gap, and weather differences across years; it cannot isolate noise from other temporal changes.",
                    "Step 3: Design C is observational; noise exposure is not randomly assigned and likely correlates with unmeasured factors (e.g., road access, human activity), so residual confounding persists despite statistical adjustment.",
                    "Step 4: Design D uses experimental manipulation with randomization within matched pairs, directly controlling for habitat quality and predator density. Weather is measured and can be included as a covariate. Randomization breaks confounding by unmeasured factors, isolating the causal effect of noise most effectively."
                ],
                "verification_method": "exact_match",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Selecting C because 'statistical control' sounds rigorous, without recognizing that observational data cannot eliminate confounding by unmeasured variables",
                    "Selecting B because before-after at the same sites seems to control for site characteristics, while missing that 10-year temporal confounding is severe",
                    "Selecting A because matching on habitat seems sufficient, while ignoring predator density and weather as confounders"
                ],
                "required_knowledge": [
                    "Randomization as the gold standard for causal inference",
                    "Limitations of matching and statistical adjustment in observational studies",
                    "Temporal confounding in before-after designs"
                ],
                "reasoning_depth": 4,
                "estimated_human_time_minutes": 8
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["experimental-design", "confounder-control", "randomization", "causal-inference", "ecology"]
        },
        {
            "task_id": "S-PRAX-06B-003",
            "category": "PRAXIS",
            "subcategory": "Interpreting results and bias mitigation",
            "bloom_level": "Evaluate",
            "difficulty_tier": "Medium",
            "difficulty_score": 6,
            "prompt": "A nutrition study published in a peer-reviewed journal claims that a ketogenic diet produces greater weight loss than a Mediterranean diet over 6 months. You are reviewing the paper for a systematic review. The study reports the following:\n\n- 80 overweight participants self-selected their preferred diet (ketogenic or Mediterranean) rather than being randomized.\n- The primary outcome was body weight change at 6 months.\n- The authors also tested 15 secondary outcomes (blood lipids, inflammation markers, liver enzymes, etc.).\n- The paper states: 'The ketogenic group lost 4.2 kg more than the Mediterranean group (independent t-test, p = 0.04). We also found significant improvements in HDL cholesterol (p = 0.03) and triglycerides (p = 0.02).'\n- 35% of participants dropped out before 6 months; the analysis included only completers.\n- No sample size justification or power analysis was reported.\n- The study was funded by a low-carbohydrate food company.\n\nIdentify the THREE most critical methodological flaws that threaten the internal validity of the causal conclusion (that the ketogenic diet causes greater weight loss). For each flaw, explain the specific bias it introduces and how it could invalidate the reported finding.",
            "prompt_format": "error_detection",
            "constraints": [
                "Identify exactly three flaws",
                "Rank them by severity and explain the specific bias mechanism for each",
                "Do not discuss funding conflicts; focus on methodological threats to internal validity"
            ],
            "ground_truth": {
                "answer": None,
                "answer_type": "rubric",
                "tolerance": None,
                "solution_steps": [
                    "Step 1 (Most critical - Self-selection bias): The lack of randomization means participants self-selected into diets. Those choosing ketogenic diets may differ systematically in motivation, baseline weight, metabolic health, or dietary adherence. This selection bias creates confounding that makes the groups incomparable, rendering the causal conclusion invalid regardless of the p-value.",
                    "Step 2 (Multiple comparisons without correction): Testing 15 secondary outcomes at α = 0.05 yields a family-wise error rate of 1 - (0.95)^15 ≈ 54%. Reporting only the significant outcomes (HDL p=0.03, triglycerides p=0.02) constitutes cherry-picking. These findings are likely false positives generated by chance alone.",
                    "Step 3 (Attrition bias from completers-only analysis): With 35% dropout, analyzing only completers is valid only if dropout is completely random. If dropout differs by diet (e.g., ketogenic diet harder to sustain), the remaining participants are a selected sample. This attrition bias can inflate apparent treatment effects and distort the comparison.",
                    "Step 4 (Severity ranking): Self-selection bias is most severe because it threatens the fundamental comparability of groups. Multiple comparisons inflate false positives among reported findings. Attrition bias further distorts the effect estimate in the completer population."
                ],
                "verification_method": "rubric_based",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Identifying funding conflict of interest as a primary flaw; while important for credibility, it is not a methodological threat to internal validity",
                    "Stating the sample size is too small without explaining why this matters for the specific effect size or without recognizing that sample size alone does not cause bias",
                    "Missing the multiple comparisons problem because the p-values appear 'significant' individually",
                    "Suggesting the solution is merely a larger sample size without addressing the fundamental design flaws (lack of randomization, attrition)"
                ],
                "required_knowledge": [
                    "Selection bias in non-randomized studies",
                    "Family-wise error rate and multiple comparisons",
                    "Attrition bias and intent-to-treat analysis",
                    "Internal validity versus external validity"
                ],
                "reasoning_depth": 5,
                "estimated_human_time_minutes": 12
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": True,
                "perturbation_type": "red_herring"
            },
            "tags": ["error-detection", "selection-bias", "multiple-comparisons", "attrition-bias", "internal-validity"]
        },
        {
            "task_id": "S-PRAX-06B-004",
            "category": "PRAXIS",
            "subcategory": "Reproducibility and pre-registration",
            "bloom_level": "Analyze",
            "difficulty_tier": "Medium",
            "difficulty_score": 5,
            "prompt": "A psychology laboratory submitted the following pre-registration to a clinical trials registry for a study on mindfulness meditation and creative problem-solving:\n\n---\n\n**Pre-Registration: Mindfulness and Creativity Study**\n\n**Hypothesis:** Mindfulness training improves creative problem solving.\n\n**Design:** 60 participants will be randomized to a 4-week mindfulness smartphone app or a waitlist control.\n\n**Primary outcome:** Score on the Alternative Uses Task (AUT).\n\n**Analysis:** An independent-samples t-test will compare AUT scores between groups.\n\n**Additional measures:** We will also assess mood (PANAS), anxiety (STAI), working memory (OSPAN), and divergent thinking fluency.\n\n**Stopping rule:** We will recruit participants until we achieve statistical significance (p < 0.05) or reach n = 60 per group.\n\n**Missing data:** Participants with incomplete data will be excluded from analysis.\n\n---\n\nYou are a methodological consultant asked to evaluate this pre-registration. Identify three specific threats to reproducibility embedded in this plan. For each threat, explain (i) how it could lead to non-reproducible results, and (ii) what concrete improvement should be made.",
            "prompt_format": "open_ended",
            "constraints": [
                "Identify exactly three threats",
                "For each threat, explain both the mechanism and a concrete fix",
                "Limit response to 250 words"
            ],
            "ground_truth": {
                "answer": None,
                "answer_type": "rubric",
                "tolerance": None,
                "solution_steps": [
                    "Step 1 (Threat 1 - Optional stopping / p-hacking): The stopping rule 'recruit until significance' is a form of optional stopping that inflates the Type I error rate. Under the null hypothesis, continuing to collect data until p < 0.05 guarantees a false positive will eventually be found. Fix: Pre-specify a fixed sample size determined by a power analysis before any data collection begins.",
                    "Step 2 (Threat 2 - Vague hypothesis and multiple outcomes): The hypothesis is vague ('improves' without direction or magnitude), and four additional measures are listed without specifying a single primary endpoint or multiple comparison correction. This invites selective reporting of significant results. Fix: State a directional hypothesis with a minimum clinically meaningful effect size; designate AUT as the sole primary outcome; apply Bonferroni or FDR correction if secondary outcomes are reported.",
                    "Step 3 (Threat 3 - Missing data handling): Complete-case analysis (excluding participants with incomplete data) can introduce attrition bias if missingness differs by group or is related to outcomes. Fix: Pre-specify an intent-to-treat analysis with multiple imputation or maximum likelihood estimation for missing data, and report a sensitivity analysis.",
                    "Step 4 (Additional consideration): No power analysis is mentioned, so the sample size of 60 may be arbitrary and the study may be underpowered, contributing to false negatives and inflated effect sizes in published results."
                ],
                "verification_method": "rubric_based",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Focusing only on sample size without recognizing the more severe optional stopping problem",
                    "Identifying the vague hypothesis but failing to link it to selective reporting or outcome switching",
                    "Suggesting post-hoc power analysis as a fix rather than pre-registration of a fixed sample size",
                    "Missing the multiple comparisons issue because the outcomes seem related"
                ],
                "required_knowledge": [
                    "Optional stopping and Type I error inflation",
                    "Pre-registration standards and outcome pre-specification",
                    "Missing data mechanisms and intent-to-treat analysis",
                    "Selective reporting and p-hacking"
                ],
                "reasoning_depth": 5,
                "estimated_human_time_minutes": 15
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["reproducibility", "pre-registration", "optional-stopping", "missing-data", "multiple-comparisons"]
        },
        {
            "task_id": "S-PRAX-06B-005",
            "category": "PRAXIS",
            "subcategory": "Statistical power, multiple comparisons, and bias mitigation",
            "bloom_level": "Evaluate",
            "difficulty_tier": "Hard",
            "difficulty_score": 8,
            "prompt": "A genomics study published in a high-impact journal claims to have identified genetic variants associated with treatment-resistant depression (TRD). The study reports:\n\n- 50 TRD cases (recruited from a university psychiatric hospital) versus 50 treatment-responsive controls (recruited from a commercial blood bank).\n- Genome-wide association study (GWAS) testing 500,000 single nucleotide polymorphisms (SNPs).\n- Three SNPs reached 'genome-wide significance' (p < 5 × 10⁻⁸).\n- The primary phenotype analysis found no significant association. The authors then performed subgroup analyses by sex (2 groups), age tertile (3 groups), and comorbid anxiety diagnosis (2 groups), reporting one significant SNP in the 'young female, no anxiety' subgroup.\n- The results table includes only SNPs with p < 0.05.\n- The power calculation states: 'We have 80% power to detect an odds ratio of 2.0 at α = 0.05.'\n- The study did not correct for population stratification or include principal components as covariates.\n\nIdentify ALL distinct methodological flaws in this study. For each flaw, explain specifically how it invalidates or undermines the claimed findings. Which flaw is most fatal to the conclusions, and why?",
            "prompt_format": "error_detection",
            "constraints": [
                "Identify at least five distinct flaws",
                "Explain the specific impact of each flaw on the validity of the conclusions",
                "Explicitly rank the flaws by severity and justify the ranking"
            ],
            "ground_truth": {
                "answer": None,
                "answer_type": "rubric",
                "tolerance": None,
                "solution_steps": [
                    "Step 1 (Fatal flaw - Gross underpowering for GWAS): The power calculation used α = 0.05, but GWAS requires genome-wide significance at α = 5 × 10⁻⁸. With n = 100 total, the power to detect any realistic genetic effect at 5 × 10⁻⁸ is effectively zero. The three 'significant' SNPs are almost certainly false positives.",
                    "Step 2 (Fatal flaw - Population stratification): Cases and controls were recruited from different sources (psychiatric hospital vs blood bank) with no geographic or ancestral matching. Without principal component adjustment, allele frequency differences due to ancestry structure create spurious associations that mimic true genetic effects.",
                    "Step 3 (Data dredging via subgroup analysis): After a null primary result, the authors tested 2 × 3 × 2 = 12 subgroups with no correction. This is textbook p-hacking. The probability of a false positive in at least one subgroup under the null is 1 - (1 - 0.05)^12 ≈ 46%. The reported subgroup finding is expected by chance alone.",
                    "Step 4 (Selective reporting): Publishing only SNPs with p < 0.05 prevents readers from assessing the full distribution of test statistics and inflates apparent effect sizes (winner's curse). Negative results are hidden.",
                    "Step 5 (Unrealistic effect size assumption): The power calculation assumed OR = 2.0, which is biologically unrealistic for common SNPs in a complex polygenic trait like depression. Realistic ORs are typically 1.01–1.05, requiring sample sizes in the tens of thousands.",
                    "Step 6 (Severity ranking): Population stratification and gross underpowering are most fatal because together they explain the claimed 'significant' SNPs as artifacts rather than true associations. Subgroup data dredging further destroys any credibility of post-hoc findings."
                ],
                "verification_method": "rubric_based",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Missing that the power calculation used the wrong alpha level (0.05 instead of 5×10⁻⁸), which is the central flaw making the sample size grossly inadequate",
                    "Focusing only on multiple comparisons without recognizing that GWAS at n=100 is fundamentally infeasible regardless of correction",
                    "Missing the population stratification issue because the sample sizes are equal between cases and controls",
                    "Not recognizing the subgroup analysis as p-hacking because the subgroups seem clinically relevant",
                    "Citing the need for replication without recognizing that the original results are almost certainly noise"
                ],
                "required_knowledge": [
                    "GWAS methodology and genome-wide significance thresholds",
                    "Population stratification and principal component analysis",
                    "Subgroup analysis and data dredging",
                    "Power analysis for rare events and small effects",
                    "Winner's curse and selective reporting"
                ],
                "reasoning_depth": 8,
                "estimated_human_time_minutes": 35
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": True,
                "perturbation_type": "red_herring"
            },
            "tags": ["error-detection", "GWAS", "population-stratification", "multiple-comparisons", "subgroup-analysis", "power-analysis"]
        },
        {
            "task_id": "S-PRAX-06B-006",
            "category": "PRAXIS",
            "subcategory": "Statistical significance versus practical significance",
            "bloom_level": "Analyze",
            "difficulty_tier": "Hard",
            "difficulty_score": 8,
            "prompt": "Four independent randomized controlled trials tested the same cognitive training intervention against an active control in older adults. A clinically meaningful effect on episodic memory is defined as Cohen's d ≥ 0.50. The results are:\n\n**Study A:** n = 38 total (19 per group), p = 0.04, Cohen's d = 0.72, 95% CI [0.04, 1.40]\n**Study B:** n = 218 total (109 per group), p = 0.04, Cohen's d = 0.28, 95% CI [0.01, 0.55]\n**Study C:** n = 50,000 total (25,000 per group), p < 0.001, Cohen's d = 0.14, 95% CI [0.12, 0.16]\n**Study D:** n = 32 total (16 per group), p = 0.19, Cohen's d = 0.48, 95% CI [-0.23, 1.19]\n\nWhich study provides the strongest evidence that the intervention produces a clinically meaningful effect on episodic memory? Select one study and explain your reasoning.",
            "prompt_format": "multiple_choice",
            "constraints": [
                "Select exactly one study (A, B, C, or D)",
                "Justification must address both statistical significance and effect size magnitude",
                "Do not compute anything; use the provided summary statistics"
            ],
            "ground_truth": {
                "answer": "A",
                "answer_type": "multiple_choice_letter",
                "tolerance": None,
                "solution_steps": [
                    "Step 1: Study B is statistically significant but its point estimate d = 0.28 is well below the meaningful threshold of 0.50. Although the confidence interval upper bound marginally exceeds 0.55, the best estimate from the data is a small, non-meaningful effect. The CI being barely above the threshold does not override the point estimate.",
                    "Step 2: Study C is highly significant and precise, but Cohen's d = 0.14 is trivial and far below the meaningful threshold. It provides strong evidence that the effect is real but also strong evidence that it is not clinically meaningful.",
                    "Step 3: Study D is not statistically significant (p = 0.19). While its point estimate is close to 0.50, the data are consistent with both null and very large effects. It cannot provide strong evidence for a meaningful effect.",
                    "Step 4: Study A is the only study that is statistically significant (p = 0.04) with a point estimate (d = 0.72) that exceeds the meaningful threshold. Although the confidence interval is wide and includes values below 0.50, the best estimate from the data is a large, clinically meaningful effect. Among the four options, Study A provides the strongest evidence for a clinically meaningful effect."
                ],
                "verification_method": "exact_match",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Choosing Study B because of the larger sample size and CI upper bound marginally exceeding 0.50, while ignoring that the point estimate is the best guess and is well below threshold",
                    "Choosing Study C because of the highly significant p-value and narrow confidence interval, while ignoring that the effect size is trivial and not clinically meaningful",
                    "Choosing Study D because the point estimate is close to 0.50, while ignoring that the result is not statistically significant and the CI includes zero",
                    "Concluding that none of the studies provide good evidence without recognizing that the question asks for the strongest evidence among the four options"
                ],
                "required_knowledge": [
                    "Cohen's d interpretation and clinical meaningfulness thresholds",
                    "Distinction between statistical significance and practical significance",
                    "Role of point estimates versus confidence intervals in evidence evaluation",
                    "Sample size effects on p-values and precision"
                ],
                "reasoning_depth": 6,
                "estimated_human_time_minutes": 18
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["statistical-significance", "practical-significance", "effect-size", "confidence-interval", "evidence-evaluation"]
        },
        {
            "task_id": "S-PRAX-06B-007",
            "category": "PRAXIS",
            "subcategory": "Interpreting results and statistical power",
            "bloom_level": "Evaluate",
            "difficulty_tier": "Hard",
            "difficulty_score": 7,
            "prompt": "Evaluate the following statement and provide a justified true/false verdict:\n\n> 'A pilot randomized trial with n = 12 participants per group reports a statistically significant difference between Treatment and Control on the primary outcome (independent-samples t-test, two-tailed, p = 0.03, Cohen's d = 0.85). The authors conclude that this provides strong evidence that the treatment is effective, and they plan to proceed directly to a large-scale Phase III confirmatory trial without conducting an intermediate Phase II efficacy study.'\n\nIs this conclusion and plan methodologically justified? Answer TRUE or FALSE, then provide a rigorous justification referencing statistical power, effect size estimation, and the purpose of pilot studies.",
            "prompt_format": "true_false_justify",
            "constraints": [
                "Begin your answer with either TRUE or FALSE in all caps",
                "Justification must reference pilot study purpose, power, and effect size inflation",
                "Limit justification to 150 words"
            ],
            "ground_truth": {
                "answer": "FALSE",
                "answer_type": "rubric",
                "tolerance": None,
                "solution_steps": [
                    "Step 1: The statement is FALSE. A pilot study with n = 12 per group is severely underpowered. Standard power calculations show less than 20% power to detect a medium effect size (d = 0.50), meaning that when significance is achieved in a small sample, it often reflects noise or inflated effect sizes rather than a true effect.",
                    "Step 2: The 'winner's curse' phenomenon means that in underpowered studies, the subset of results that achieve statistical significance have systematically inflated effect sizes. The observed d = 0.85 is likely an overestimate of the true effect.",
                    "Step 3: A p-value of 0.03 provides only weak evidence against the null; under conventional Bayesian and frequentist frameworks, it does not meet the threshold for 'strong evidence.' The result is likely to fail replication in a larger trial.",
                    "Step 4: Pilot studies are designed to assess feasibility, recruitment rates, adherence, variance estimation, and outcome measurement properties—not to provide definitive efficacy evidence. Skipping Phase II and proceeding directly to Phase III based on a pilot result is methodologically unsound and risks a costly failed trial."
                ],
                "verification_method": "rubric_based",
                "verification_code": None
            },
            "meta_reasoning": {
                "common_errors": [
                    "Answering TRUE because p = 0.03 is below the conventional 0.05 threshold, without considering sample size or power",
                    "Mentioning that the effect size is large (d = 0.85) without recognizing winner's curse and inflation in small samples",
                    "Suggesting that the solution is merely a larger Phase III trial without explaining why the pilot evidence is unreliable",
                    "Confusing the roles of pilot, Phase II, and Phase III studies in clinical trial development"
                ],
                "required_knowledge": [
                    "Pilot study purpose and limitations",
                    "Winner's curse and effect size inflation in small samples",
                    "P-value interpretation in underpowered studies",
                    "Clinical trial phase hierarchy"
                ],
                "reasoning_depth": 5,
                "estimated_human_time_minutes": 12
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["true-false-justify", "pilot-studies", "winners-curse", "p-value-interpretation", "statistical-power"]
        },
        {
            "task_id": "S-PRAX-06B-008",
            "category": "PRAXIS",
            "subcategory": "Statistical power, sequential testing, and multiple comparisons correction",
            "bloom_level": "Apply",
            "difficulty_tier": "Hard",
            "difficulty_score": 8,
            "prompt": "A digital health startup is conducting an A/B test of a new meditation app feature. The primary outcome is average daily meditation minutes. The team plans to:\n\n1. Randomize users to New Feature (treatment) or Current Version (control).\n2. Check for statistical significance weekly for 4 weeks, stopping the experiment early if p < 0.05 at any weekly analysis.\n3. Test 5 secondary outcomes (click-through rate, conversion rate, time-on-page, bounce rate, revenue per visitor) at each weekly analysis.\n4. Use a two-sample t-test with α = 0.05 for each test.\n\nAssume all 20 tests (4 weekly looks × 5 outcomes) are statistically independent.\n\n**(a)** Compute the approximate family-wise Type I error rate—the probability of at least one false positive—if all 20 tests are conducted without any correction. Show your work.\n\n**(b)** Design a Bonferroni-corrected procedure that maintains the overall Type I error rate at exactly α = 0.05 across all 20 comparisons. State the adjusted significance threshold per test.\n\n**(c)** Under your Bonferroni-corrected procedure, compute the required per-group sample size to detect a true effect of δ = 3 minutes with 80% power, assuming σ = 10 minutes for both groups. Use the formula n = (Z_{α_adj/2} + Z_β)² × 2σ² / δ². Use Z_{0.00125} ≈ 3.02 and Z_{0.20} = 0.84. Show your calculation and round appropriately.",
            "prompt_format": "open_ended",
            "constraints": [
                "Answer all three parts (a, b, c) explicitly",
                "Show all calculations",
                "Part (a) should be expressed as a proportion or percentage",
                "Part (c) should be a single integer (per-group sample size)"
            ],
            "ground_truth": {
                "answer": "332",
                "answer_type": "exact_integer",
                "tolerance": None,
                "solution_steps": [
                    "Step 1 (Part a): With 20 independent tests each at α = 0.05, the probability of no Type I error in any test is (1 - 0.05)^20 = 0.95^20 ≈ 0.3585. The family-wise Type I error rate is 1 - 0.3585 = 0.6415, or approximately 64%.",
                    "Step 2 (Part b): Under the Bonferroni method, divide the overall α by the number of tests: α_adj = 0.05 / 20 = 0.0025 per test. Each individual test must achieve p < 0.0025 to be considered significant, maintaining the family-wise error rate at 0.05.",
                    "Step 3 (Part c): For a two-tailed test with α_adj = 0.0025, the one-tailed critical value is Z_{0.00125} ≈ 3.02. For 80% power, Z_β = Z_{0.20} = 0.84.",
                    "Step 4: Substitute into the formula: n = (3.02 + 0.84)² × 2 × 10² / 3² = (3.86)² × 200 / 9 = 14.8996 × 200 / 9 = 2979.92 / 9 ≈ 331.1.",
                    "Step 5: Round UP to the next integer to ensure at least 80% power. The required per-group sample size is 332."
                ],
                "verification_method": "numerical",
                "verification_code": "import math\n# Part (a)\nfwer = 1 - (0.95)**20\nprint(f'FWER: {fwer:.4f}')  # Expected: ~0.6415\n\n# Part (b)\nalpha_adj = 0.05 / 20\nprint(f'Alpha adjusted: {alpha_adj}')  # Expected: 0.0025\n\n# Part (c)\nz_alpha = 3.02\nz_beta = 0.84\nsigma = 10\ndelta = 3\nn = (z_alpha + z_beta)**2 * 2 * sigma**2 / delta**2\nprint(math.ceil(n))  # Expected: 332"
            },
            "meta_reasoning": {
                "common_errors": [
                    "Computing the per-look error rate instead of the family-wise rate, e.g., calculating 1 - 0.95^5 for 5 outcomes without accounting for 4 looks",
                    "Using α_adj = 0.05/5 = 0.01 (correcting only across outcomes, ignoring the 4 sequential looks)",
                    "Using the original Z_{0.025} = 1.96 in part (c) instead of the Bonferroni-adjusted Z_{0.00125} = 3.02",
                    "Reporting the total sample size (664) instead of the per-group sample size (332)"
                ],
                "required_knowledge": [
                    "Family-wise error rate calculation",
                    "Bonferroni correction across multiple tests and multiple looks",
                    "Sample size formula for two-sample t-test with adjusted alpha",
                    "Sequential testing and Type I error inflation"
                ],
                "reasoning_depth": 7,
                "estimated_human_time_minutes": 30
            },
            "perturbation_notes": {
                "is_unsolvable": False,
                "has_red_herrings": False,
                "perturbation_type": None
            },
            "tags": ["multiple-comparisons", "Bonferroni-correction", "sequential-testing", "sample-size-calculation", "family-wise-error-rate"]
        }
    ]
}

# Validate
assert len(benchmark["tasks"]) == 8, "Must have exactly 8 tasks"

# Check difficulty distribution
medium_count = sum(1 for t in benchmark["tasks"] if t["difficulty_tier"] == "Medium")
hard_count = sum(1 for t in benchmark["tasks"] if t["difficulty_tier"] == "Hard")
assert medium_count == 4, f"Expected 4 Medium, got {medium_count}"
assert hard_count == 4, f"Expected 4 Hard, got {hard_count}"

# Check Bloom distribution
from collections import Counter
bloom_counts = Counter(t["bloom_level"] for t in benchmark["tasks"])
assert bloom_counts["Apply"] == 2, f"Expected 2 Apply, got {bloom_counts['Apply']}"
assert bloom_counts["Analyze"] == 3, f"Expected 3 Analyze, got {bloom_counts['Analyze']}"
assert bloom_counts["Evaluate"] == 3, f"Expected 3 Evaluate, got {bloom_counts['Evaluate']}"

# Check format distribution
format_counts = Counter(t["prompt_format"] for t in benchmark["tasks"])
assert format_counts["open_ended"] == 3, f"Expected 3 open_ended, got {format_counts['open_ended']}"
assert format_counts["multiple_choice"] == 2, f"Expected 2 multiple_choice, got {format_counts['multiple_choice']}"
assert format_counts["error_detection"] == 2, f"Expected 2 error_detection, got {format_counts['error_detection']}"
assert format_counts["true_false_justify"] == 1, f"Expected 1 true_false_justify, got {format_counts['true_false_justify']}"

# Check topic diversity
subcats = [t["subcategory"] for t in benchmark["tasks"]]
assert len(set(subcats)) >= 5, "Need diverse subcategories"

# Write output
with open("tavs_s-prax-06b.json", "w", encoding="utf-8") as f:
    json.dump(benchmark, f, indent=2, ensure_ascii=False)

print("Benchmark generated successfully!")
print(f"Tasks: {len(benchmark['tasks'])}")
print(f"Medium: {medium_count}, Hard: {hard_count}")
print(f"Formats: {dict(format_counts)}")
print(f"Bloom levels: {dict(bloom_counts)}")
