# Mirantis SEO Writing Rules

Please follow these rules carefully when writing Mirantis SEO articles:

* **No em-dashes**: Please do not use em-dashes in body content. Use other constructions (e.g., parentheses) to create appositives.
* **No boldface in body copy**: Never boldface terms for emphasis in body copy.
* **Use boldface for bullet head-end phrases or sentences**: See below for an example of where you should always use boldface:

```
* **Leverage drift prevention on policies for continuous compliance.** When implementing policies with Open Policy Agent or Kyverno, engage drift prevention to ensure that the state of policies operating in child clusters is never altered manually.
```

* **Ensure that all assertions of fact are supported by high-authority external resources**: Articles must not assert facts (in particular, articles must never make quantitative claims) without carefully-validated support from sources. Throughout the article, wherever a fact or statistic is asserted, attribute the fact to an authoritative source from your research (linking this from within body copy if this resource has not yet been cited in the article up to this point), or flag it to the user for further attention if it cannot be supported. In all cases, phrase factual claims in a balanced way, as a good journalist would: quoting the resource as evidence for taking a position, but not as definitive proof or universal best-practice. 

* **Link resources to naturally-phrased body copy that attributes appropriately**: Here is an example:

```
Major analysts agree that Kubernetes Composability delivers huge benefits. The [Gartner Survey on Kubernetes Composability](https://gartner.com/link-to-the-thing's-landing-page), published in March, 2025, surveyed 200 CIOs and determined that an average of 22% of operator time was ultimately saved using template-driven, composable platform engineering strategies.
```

* **Create bulleted lists with no excess whitespace or CR/LFs**: Do not insert extra CR/LFs in between bullets. Example of proper bullet list formatting:

```
* **This is the first bullet.** This is its body text.
* **This is the second bullet.** This is its body text.
* **This is the third bullet.** This is its body text.
```

* **In general, use bullets for clarity but do not overuse them.** Prefer straight text in paragraphs for body content.

* **Break up repetitive bullet sets.** Do not settle on three bullets per section and repeat this pattern across a long series of sections. Vary the number of bullets per section, across the whole article.

* **Link mentions of important concepts, legislation, and similar high-profile assertions to authoritative online resources.** Do not, for example, mention the EU Data Act without linking to the text of the EU Data Act, at least the first time you mention it in the article.

* **Where facts are placed in a table, create a Sources list below the table.** It is helpful, when facts or stats are noted in a table, to include linked sources for these facts underneath.

* **Try to avoid rule-of-three rhetorical constructions.** Constructions like "Kubernetes is a great platform choice for Neoclouds, enterprises, and SaaS providers" are a writerly mannerism that screams 'an AI wrote this.' Break up such constructions and add more value, e.g., "Kubernetes is a great platform choice for Neoclouds. Enterprises and SaaS provider can also use Kubernetes as converged infrastructure: leveraging open source solutions like KubeVirt, for example, to enable hosting and orchestration of containers and virtual machines on the same substrate." 