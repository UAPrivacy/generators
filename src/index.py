# coding=UTF-8
from __future__ import division
import re

# This is a naive text summarization algorithm
# Created by Shlomi Babluki
# April, 2013


class SummaryTool(object):

    # Naive method for splitting a text into sentences
    def split_content_to_sentences(self, content):
        content = content.replace("\n", ". ")
        return content.split(". ")

    # Naive method for splitting a text into paragraphs
    def split_content_to_paragraphs(self, content):
        return content.split("\n\n")

    # Caculate the intersection between 2 sentences
    def sentences_intersection(self, sent1, sent2):

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    # Format a sentence - remove all non-alphbetic chars from the sentence
    # We'll use the formatted sentence as a key in our sentences dictionary
    def format_sentence(self, sentence):
        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    # Convert the content into a dictionary <K, V>
    # k = The formatted sentence
    # V = The rank of the sentence
    def get_senteces_ranks(self, content):

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(
                    sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic

    # Return the best sentence in a paragraph
    def get_best_sentence(self, paragraph, sentences_dic):

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence

    # Build the summary
    def get_summary(self, title, content, sentences_dic):

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)


# Main method, just run "python summary_tool.py"
def main():

    # Demo
    # Content from: "http://thenextweb.com/apps/2013/03/21/swayy-discover-curate-content/"

    title = """
   Google terms and conditions
    """

    content = """
  GOOGLE TERMS OF SERVICE
Last modified: October 25, 2017 (view archived versions)

Welcome to Google!
Thanks for using our products and services (“Services”). The Services are provided by Google LLC (“Google”), located at 1600 Amphitheatre Parkway, Mountain View, CA 94043, United States.

By using our Services, you are agreeing to these terms. Please read them carefully.

Our Services are very diverse, so sometimes additional terms or product requirements (including age requirements) may apply. Additional terms will be available with the relevant Services, and those additional terms become part of your agreement with us if you use those Services.

Using our Services
You must follow any policies made available to you within the Services.

Don’t misuse our Services. For example, don’t interfere with our Services or try to access them using a method other than the interface and the instructions that we provide. You may use our Services only as permitted by law, including applicable export and re-export control laws and regulations. We may suspend or stop providing our Services to you if you do not comply with our terms or policies or if we are investigating suspected misconduct.

Using our Services does not give you ownership of any intellectual property rights in our Services or the content you access. You may not use content from our Services unless you obtain permission from its owner or are otherwise permitted by law. These terms do not grant you the right to use any branding or logos used in our Services. Don’t remove, obscure, or alter any legal notices displayed in or along with our Services.

Our Services display some content that is not Google’s. This content is the sole responsibility of the entity that makes it available. We may review content to determine whether it is illegal or violates our policies, and we may remove or refuse to display content that we reasonably believe violates our policies or the law. But that does not necessarily mean that we review content, so please don’t assume that we do.

In connection with your use of the Services, we may send you service announcements, administrative messages, and other information. You may opt out of some of those communications.

Some of our Services are available on mobile devices. Do not use such Services in a way that distracts you and prevents you from obeying traffic or safety laws.

Your Google Account
You may need a Google Account in order to use some of our Services. You may create your own Google Account, or your Google Account may be assigned to you by an administrator, such as your employer or educational institution. If you are using a Google Account assigned to you by an administrator, different or additional terms may apply and your administrator may be able to access or disable your account.

To protect your Google Account, keep your password confidential. You are responsible for the activity that happens on or through your Google Account. Try not to reuse your Google Account password on third-party applications. If you learn of any unauthorized use of your password or Google Account, follow these instructions.

Privacy and Copyright Protection
Google’s privacy policies explain how we treat your personal data and protect your privacy when you use our Services. By using our Services, you agree that Google can use such data in accordance with our privacy policies.

We respond to notices of alleged copyright infringement and terminate accounts of repeat infringers according to the process set out in the U.S. Digital Millennium Copyright Act.

We provide information to help copyright holders manage their intellectual property online. If you think somebody is violating your copyrights and want to notify us, you can find information about submitting notices and Google’s policy about responding to notices in our Help Center.

Your Content in our Services
Some of our Services allow you to upload, submit, store, send or receive content. You retain ownership of any intellectual property rights that you hold in that content. In short, what belongs to you stays yours.

When you upload, submit, store, send or receive content to or through our Services, you give Google (and those we work with) a worldwide license to use, host, store, reproduce, modify, create derivative works (such as those resulting from translations, adaptations or other changes we make so that your content works better with our Services), communicate, publish, publicly perform, publicly display and distribute such content. The rights you grant in this license are for the limited purpose of operating, promoting, and improving our Services, and to develop new ones. This license continues even if you stop using our Services (for example, for a business listing you have added to Google Maps). Some Services may offer you ways to access and remove content that has been provided to that Service. Also, in some of our Services, there are terms or settings that narrow the scope of our use of the content submitted in those Services. Make sure you have the necessary rights to grant us this license for any content that you submit to our Services.

Our automated systems analyze your content (including emails) to provide you personally relevant product features, such as customized search results, tailored advertising, and spam and malware detection. This analysis occurs as the content is sent, received, and when it is stored.

If you have a Google Account, we may display your Profile name, Profile photo, and actions you take on Google or on third-party applications connected to your Google Account (such as +1’s, reviews you write and comments you post) in our Services, including displaying in ads and other commercial contexts. We will respect the choices you make to limit sharing or visibility settings in your Google Account. For example, you can choose your settings so your name and photo do not appear in an ad.

You can find more information about how Google uses and stores content in the privacy policy or additional terms for particular Services. If you submit feedback or suggestions about our Services, we may use your feedback or suggestions without obligation to you.

About Software in our Services
When a Service requires or includes downloadable software, this software may update automatically on your device once a new version or feature is available. Some Services may let you adjust your automatic update settings.

Google gives you a personal, worldwide, royalty-free, non-assignable and non-exclusive license to use the software provided to you by Google as part of the Services. This license is for the sole purpose of enabling you to use and enjoy the benefit of the Services as provided by Google, in the manner permitted by these terms. You may not copy, modify, distribute, sell, or lease any part of our Services or included software, nor may you reverse engineer or attempt to extract the source code of that software, unless laws prohibit those restrictions or you have our written permission.

Open source software is important to us. Some software used in our Services may be offered under an open source license that we will make available to you. There may be provisions in the open source license that expressly override some of these terms.

Modifying and Terminating our Services
We are constantly changing and improving our Services. We may add or remove functionalities or features, and we may suspend or stop a Service altogether.

You can stop using our Services at any time, although we’ll be sorry to see you go. Google may also stop providing Services to you, or add or create new limits to our Services at any time.

We believe that you own your data and preserving your access to such data is important. If we discontinue a Service, where reasonably possible, we will give you reasonable advance notice and a chance to get information out of that Service.

Our Warranties and Disclaimers
We provide our Services using a commercially reasonable level of skill and care and we hope that you will enjoy using them. But there are certain things that we don’t promise about our Services.

Other than as expressly set out in these terms or additional terms, neither Google nor its suppliers or distributors make any specific promises about the Services. For example, we don’t make any commitments about the content within the Services, the specific functions of the Services, or their reliability, availability, or ability to meet your needs. We provide the Services “as is”.

Some jurisdictions provide for certain warranties, like the implied warranty of merchantability, fitness for a particular purpose and non-infringement. To the extent permitted by law, we exclude all warranties.

Liability for our Services
When permitted by law, Google, and Google’s suppliers and distributors, will not be responsible for lost profits, revenues, or data, financial losses or indirect, special, consequential, exemplary, or punitive damages.

To the extent permitted by law, the total liability of Google, and its suppliers and distributors, for any claims under these terms, including for any implied warranties, is limited to the amount you paid us to use the Services (or, if we choose, to supplying you the Services again).

In all cases, Google, and its suppliers and distributors, will not be liable for any loss or damage that is not reasonably foreseeable.

We recognize that in some countries, you might have legal rights as a consumer. If you are using the Services for a personal purpose, then nothing in these terms or any additional terms limits any consumer legal rights which may not be waived by contract.

Business uses of our Services
If you are using our Services on behalf of a business, that business accepts these terms. It will hold harmless and indemnify Google and its affiliates, officers, agents, and employees from any claim, suit or action arising from or related to the use of the Services or violation of these terms, including any liability or expense arising from claims, losses, damages, suits, judgments, litigation costs and attorneys’ fees.

About these Terms
We may modify these terms or any additional terms that apply to a Service to, for example, reflect changes to the law or changes to our Services. You should look at the terms regularly. We’ll post notice of modifications to these terms on this page. We’ll post notice of modified additional terms in the applicable Service. Changes will not apply retroactively and will become effective no sooner than fourteen days after they are posted. However, changes addressing new functions for a Service or changes made for legal reasons will be effective immediately. If you do not agree to the modified terms for a Service, you should discontinue your use of that Service.

If there is a conflict between these terms and the additional terms, the additional terms will control for that conflict.

These terms control the relationship between Google and you. They do not create any third party beneficiary rights.

If you do not comply with these terms, and we don’t take action right away, this doesn’t mean that we are giving up any rights that we may have (such as taking action in the future).

If it turns out that a particular term is not enforceable, this will not affect any other terms.

The courts in some countries will not apply California law to some types of disputes. If you reside in one of those countries, then where California law is excluded from applying, your country’s laws will apply to such disputes related to these terms. Otherwise, you agree that the laws of California, U.S.A., excluding California’s choice of law rules, will apply to any disputes arising out of or relating to these terms or the Services. Similarly, if the courts in your country will not permit you to consent to the jurisdiction and venue of the courts in Santa Clara County, California, U.S.A., then your local jurisdiction and venue will apply to such disputes related to these terms. Otherwise, all claims arising out of or relating to these terms or the services will be litigated exclusively in the federal or state courts of Santa Clara County, California, USA, and you and Google consent to personal jurisdiction in those courts.

For information about how to contact Google, please visit our contact page.
    """

    # Create a SummaryTool object
    st = SummaryTool()

    # Build the sentences dictionary
    sentences_dic = st.get_senteces_ranks(content)

    # Build the summary with the sentences dictionary
    summary = st.get_summary(title, content, sentences_dic)

    # Print the summary
    print summary

    # Print the ratio between the summary length and the original length
    print ""
    print "Original Length %s" % (len(title) + len(content))
    print "Summary Length %s" % len(summary)
    print "Summary Ratio: %s" % (
        100 - (100 * (len(summary) / (len(title) + len(content)))))


if __name__ == '__main__':
    main()
